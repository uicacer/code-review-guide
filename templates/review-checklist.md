# Review Checklist

A printable checklist for the human layers of the [protocol](../PROTOCOL.md). Go in order; don't sweat the small stuff until the big stuff is clear. New terms: [Glossary](../GLOSSARY.md).

---

## Layer 4 — Human review (every PR)

**Correctness & design**
- [ ] Does it actually solve the stated problem?
- [ ] Does it fit the existing architecture (not fight it)?
- [ ] Edge cases handled: empty input, nulls, errors, boundaries?
- [ ] Idempotent / safe to run twice where that matters?

**Tests**
- [ ] Tests exist for the new logic?
- [ ] They cover the edge cases, not just the happy path?
- [ ] Is there *proof it ran* (output/screenshot), not just "it compiles"?

**Readability**
- [ ] Will a stranger understand this in 6 months?
- [ ] Names clear? No dead or commented-out code?
- [ ] Non-obvious decisions explained (a short "why" comment)?

**Size & style**
- [ ] Under ~400 changed lines (if not, ask to split)?
- [ ] Style/formatting is automated — I'm not commenting on it.

**Process**
- [ ] Comments use Conventional Comments (`issue:`, `suggestion:`, `nitpick:`, …) with `(blocking)`/`(non-blocking)`.
- [ ] Responding within one business day.

---

## Layer 5 — Adversarial & PHI pass (data / auth / PHI / ML / secure compute)

**STRIDE-lite — attacker hat on:**
- [ ] **S**poofing — could someone impersonate a user/service here?
- [ ] **T**ampering — could someone change data they shouldn't?
- [ ] **R**epudiation — is there a log proving who did what?
- [ ] **I**nformation disclosure — any PHI leak in logs, errors, URLs, test data?
- [ ] **D**enial of service — could this be overwhelmed or crashed?
- [ ] **E**levation of privilege — could someone gain more access than intended?

**Secrets & data**
- [ ] No secrets (keys/passwords/tokens) in code or git history (secret scan clean)?
- [ ] Test fixtures use **synthetic** data — no real patient records / MRNs?
- [ ] PHI absent from logs, error messages, URLs, metrics, and resource tags?

**Access & crypto**
- [ ] Least-privilege IAM (no wildcard permissions)?
- [ ] Encrypted at rest (KMS) and in transit (TLS 1.2+)?
- [ ] Audit logging (e.g., CloudTrail) on?

**Inputs & dependencies**
- [ ] All external input validated (incl. FHIR search params); injection-safe?
- [ ] New dependencies actually exist, are pinned, and scanned for vulnerabilities?
- [ ] Any AI-generated section verified for hallucinated APIs / insecure defaults?

**Blue-team follow-up**
- [ ] For each risk found: would our logs/alerts catch it? If not → detection gap filed.

---

## ML / reproducibility (if the PR trains or serves a model)
- [ ] No train/test leakage; split at the patient level?
- [ ] Seeds fixed; environment pinned; data + model versioned?
- [ ] Model card + dataset datasheet present/updated?
- [ ] Drift/monitoring considered for anything deployed?

---

## Solo quick-pass
When you're the only developer, before merging your own PR:
- [ ] Pre-commit + CI green
- [ ] Read my own diff after a break, by this checklist
- [ ] 15-min attacker pass (out loud) on anything touching data
- [ ] I can explain every line, including anything AI wrote
