<!--
Pull request template.
To use: save as .github/pull_request_template.md in your repo.
GitHub will pre-fill every new PR with this. Delete the italic hints as you fill it in.
-->

## What changed
<!-- One short paragraph. What does this PR do? -->

## Why
<!-- Link an issue, or explain the motivation. -->

## How to test
<!-- Steps a reviewer can follow to verify it works. -->

## Proof it runs
<!-- Paste test output, a screenshot, or logs. "It compiles" is not proof. -->

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change (schema / API / data format)
- [ ] Infrastructure / config
- [ ] Docs

## AI disclosure
- [ ] No AI assistance
- [ ] AI-assisted - the parts I am least sure about: <!-- name files/functions -->
<!-- I have read and understood every line I am submitting. -->

## Security & PHI checklist (required if this touches data / auth / patient info)
- [ ] No secrets (keys, passwords, tokens) in the code or history
- [ ] No PHI in logs, errors, URLs, or test data; test fixtures use synthetic data
- [ ] Access is least-privilege; data encrypted at rest and in transit
- [ ] I ran a STRIDE-lite adversary pass (see docs/03-adversarial-review.md)

## Rollback plan
<!-- How do we revert this if it breaks production? -->
