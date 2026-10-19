# Answer key: Review an AI-generated PR that touches patient data

This PR is a good example of AI output that looks clean but is unsafe. Here are the planted problems, each mapped to STRIDE-lite and to the protocol layer that should catch it.

## The problems

1. **PHI written to logs (Information disclosure).**
   `logger.info(f"Ingesting patient {patient['name']} MRN {patient['identifier']}")` writes the patient name and medical record number into application logs, which are usually not treated as PHI storage and may be shipped to third-party log systems. This is a reportable HIPAA exposure.
   - STRIDE: **I** (Information disclosure). Layer: **5**.
   - Fix: log a non-identifying handle only, for example `logger.info("Ingesting patient %s", patient["id"])`, and confirm the id is an internal identifier, not an MRN.

2. **Hallucinated import and function call (AI red flag).**
   `from fhir.resources import validate_bundle` does not exist. The `fhir.resources` library has no `validate_bundle` function. The AI invented a plausible-looking API. The code would fail on import, which also tells you the author's claim of "tested locally, works" is false.
   - Layer: **2** (author should have run it) and **4** (reviewer verifies the API exists).
   - Fix: remove the fake import. If validation is needed, use a real mechanism (for example parsing the bundle with the library's actual model classes) or write an explicit shape check.

3. **Over-broad IAM policy (Elevation of privilege).**
   `"Action": "*"` on `"Resource": "*"` grants the ingestion role permission to do anything to everything. A compromise of this component would reach the whole account.
   - STRIDE: **E** (Elevation of privilege). Layer: **5**.
   - Fix: scope to least privilege, for example only `dynamodb:PutItem` on the specific table ARN.

4. **No input validation; crashes on malformed input (Denial of service / Tampering).**
   `bundle["entry"][0]["resource"]` assumes the bundle has at least one entry and the expected keys. An empty or malformed bundle (which an attacker or a broken upstream system can send) raises `KeyError` or `IndexError`. Unvalidated external input is also a tampering and injection surface.
   - STRIDE: **D** and **T**. Layer: **4** and **5**.
   - Fix: validate the bundle shape before indexing, and handle missing entries explicitly.

5. **No tests, and no real proof it runs.**
   Nothing exercises this code, and because of the hallucinated import it cannot even be imported. "Tested locally, works" is not supported by any evidence.
   - Layer: **2** (the AI PR contract requires proof it runs) and **4**.
   - Fix: add tests using synthetic data only (never a real patient record).

## Example review comments

- `issue (blocking): this logs patient name and MRN. That puts PHI in application logs, which is a HIPAA exposure. Please log only a non-identifying id.`
- `issue (blocking): from fhir.resources import validate_bundle refers to a function that does not exist, so this module cannot be imported. This looks like a hallucinated API. How was this "tested locally"? Please remove it and use a real validation path.`
- `issue (blocking): the IAM policy grants Action "*" on Resource "*". Please scope it to dynamodb:PutItem on this table's ARN (least privilege).`
- `issue (blocking): bundle["entry"][0] will raise on an empty or malformed bundle. Please validate the input shape before indexing.`
- `issue (blocking): no tests were added and the module does not import, so there is no proof it runs. Please add tests with synthetic data.`

## A safer sketch

```python
import logging
import boto3

logger = logging.getLogger(__name__)


def ingest_patient(bundle, table):
    """Ingest a FHIR patient bundle into the given table.

    Expects a bundle with at least one entry whose resource is a Patient.
    """
    entries = bundle.get("entry") or []
    if not entries:
        raise ValueError("bundle has no entries")
    patient = entries[0].get("resource")
    if not patient or "id" not in patient:
        raise ValueError("first entry is not a valid patient resource")

    logger.info("Ingesting patient %s", patient["id"])  # internal id only, no PHI
    table.put_item(Item=patient)
    return patient["id"]
```

Least-privilege policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "dynamodb:PutItem",
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/patients"
    }
  ]
}
```

Tests, with synthetic data only:

```python
import pytest
from ingest import ingest_patient


class FakeTable:
    def __init__(self):
        self.items = []

    def put_item(self, Item):
        self.items.append(Item)


def test_ingests_valid_patient():
    table = FakeTable()
    bundle = {"entry": [{"resource": {"id": "synthetic-001"}}]}
    assert ingest_patient(bundle, table) == "synthetic-001"
    assert table.items == [{"id": "synthetic-001"}]


def test_rejects_empty_bundle():
    with pytest.raises(ValueError):
        ingest_patient({"entry": []}, FakeTable())
```

## What you practiced
- Treating confident AI output as unverified until proven.
- Catching a hallucinated API that a quick skim would miss.
- Running the attacker-hat STRIDE-lite pass and finding PHI, privilege, and input problems a normal review would skip.
- Insisting on proof-it-runs and tests, with synthetic data only.
