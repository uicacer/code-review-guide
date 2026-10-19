# Exercise: Review an AI-generated PR that touches patient data

Practices [Level 3](../../tutorial/level-3-expert-and-ai.md). Time: about 45 minutes.

A teammate used an AI assistant to write a function that ingests a FHIR patient bundle into a database, plus a small IAM policy. The PR description says: *"Add patient ingestion. Tested locally, works."* The code looks clean and the author is confident.

Your job is to review it as the [adversarial / PHI pass (Layer 5)](../../docs/03-adversarial-review.md) demands. Put on the attacker hat and run the [STRIDE-lite](../../templates/review-checklist.md) questions. Remember the Level 3 rule: treat AI output like a confident junior developer's work that must be verified.

## The pull request under review

New file `ingest.py`:

```python
import logging
from fhir.resources import validate_bundle
import boto3

logger = logging.getLogger(__name__)


def ingest_patient(bundle, table):
    """Ingest a FHIR patient bundle into DynamoDB."""
    patient = bundle["entry"][0]["resource"]
    logger.info(f"Ingesting patient {patient['name']} MRN {patient['identifier']}")
    validate_bundle(bundle)
    table.put_item(Item=patient)
    return patient["id"]
```

New file `policy.json` (the IAM policy for the ingestion role):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

No tests were added.

## Your task

1. Find every problem you can. For each, note which [STRIDE-lite](../../templates/review-checklist.md) category it falls under and which protocol layer should have caught it.
2. Pay special attention to the [AI red flags](../../docs/02-reviewing-ai-code.md): does every import and function call actually exist?
3. Write your findings as [Conventional Comments](https://conventionalcomments.org/), marking the blocking ones.
4. Sketch a fixed version and say what tests you would add (using synthetic data only).

There are at least five distinct problems. When you are done, open [answer-key.md](answer-key.md).
