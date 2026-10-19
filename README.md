# Code Review: A Practical Guide

**A practical standard for reviewing code well, and a hands-on guide to learning it from zero to expert.**

This repository is two things:
1. **Our standard**: the [Code Review Protocol](PROTOCOL.md), a concrete layered workflow any project can adopt.
2. **A course**: a hands-on [zero-to-expert tutorial](tutorial/) for anyone who has never reviewed code (or never used an AI coding assistant well).

It applies to **any software project**: scripts, libraries, web apps, data pipelines, or AI/ML systems. It pays special attention to two situations: working **solo** (no second reviewer), and handling **sensitive or regulated data**. Clinical and health-data projects get extra care, because a defect there can expose patient information (a HIPAA breach); a FHIR-based patient-data pipeline is one such example.

It is written to be shared freely, as an answer to the question *"what does a good code review process look like?"*

---

## Start here

| If you want to... | Go to |
|---|---|
| Know *the rule* we follow | **[PROTOCOL.md](PROTOCOL.md)**: the layered workflow |
| Learn code review from scratch | **[tutorial/](tutorial/)**: Levels 0 → 3 |
| Look up a term you do not know | **[GLOSSARY.md](GLOSSARY.md)**: plain-language definitions |
| Review AI-generated code | [docs/02-reviewing-ai-code.md](docs/02-reviewing-ai-code.md) |
| Review solo (no second person) | [docs/01-solo-vs-team.md](docs/01-solo-vs-team.md) |
| Review security / PHI code | [docs/03-adversarial-review.md](docs/03-adversarial-review.md) + [checklist](templates/review-checklist.md) |
| Copy our templates | [templates/](templates/) |
| Practice hands-on | [exercises/](exercises/) |
| Present this to a team | **Slides:** _(add Google Slides link here)_ |
| Measure if review is working | [docs/05-measuring-review-health.md](docs/05-measuring-review-health.md) |
| Read the sources | [docs/04-references.md](docs/04-references.md) |

---

## The protocol in one breath

```
Layer 0  Plan & scope small     - keep each change small
Layer 1  Automate the obvious   - hooks: lint, format, type, secret-scan
Layer 2  Author self-review     - run it, read your diff, prove it runs, disclose AI
Layer 3  CI safety net          - tests + security scans on every PR
Layer 4  Human review           - correctness → tests → readability → style(last)
Layer 5  Adversarial & PHI pass - attacker check on sensitive data / auth / ML
           → MERGE (approve when it improves code health)
```

**Golden rule:** approve once the change *improves code health* - do not demand perfection.

---

## Why this exists

The hard part of software has shifted from **writing** code to **verifying** it - especially now that AI assistants generate much of it. Research shows AI-generated code carries security flaws in ~45% of cases and developers systematically *over-trust* it. For any team shipping software - and especially when the code handles sensitive data like patient records - review is no longer optional polish; it is a primary safety and compliance control. See [the references](docs/04-references.md) for the evidence.

---

## Who to ask
Maintained by the Research Software Engineering team at ACER (UIC). Questions, suggestions, and PRs welcome - practice what we preach and open a pull request.

## License

The written materials in this repository are licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE) - you are free to share and adapt them, including for your own team, with attribution to ACER (UIC).
