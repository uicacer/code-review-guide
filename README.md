# ACER Code Review

**How we review code at ACER — and how to learn to do it well, from zero to expert.**

This repository is two things:
1. **Our standard** — the [ACER Code Review Protocol](PROTOCOL.md), a concrete layered workflow any project can adopt.
2. **A course** — a hands-on [zero-to-expert tutorial](tutorial/) for anyone who has never reviewed code (or never used an AI coding assistant well).

It applies to **any software project** — scripts, libraries, web apps, data pipelines, or AI/ML systems. It pays special attention to two situations common at ACER: working **solo** (no second reviewer), and handling **sensitive or regulated data**. Health-data projects get extra care, because a defect there can expose patient information (a HIPAA breach) — AIHealth4All (AWS HealthLake / FHIR) is one such example.

It also serves as our shareable answer when someone asks *“what is ACER's code review process?”*

---

## Start here

| If you want to… | Go to |
|---|---|
| Know *the rule* we follow | **[PROTOCOL.md](PROTOCOL.md)** — the layered workflow |
| Learn code review from scratch | **[tutorial/](tutorial/)** — Levels 0 → 3 |
| Look up a term you don't know | **[GLOSSARY.md](GLOSSARY.md)** — plain-language definitions |
| Review AI-generated code | [docs/02-reviewing-ai-code.md](docs/02-reviewing-ai-code.md) |
| Review solo (no second person) | [docs/01-solo-vs-team.md](docs/01-solo-vs-team.md) |
| Review security / PHI code | [docs/03-adversarial-review.md](docs/03-adversarial-review.md) + [checklist](templates/review-checklist.md) |
| Copy our templates | [templates/](templates/) |
| Present this to a team | **Slides:** _(add Google Slides link here)_ |
| Read the sources | [docs/04-references.md](docs/04-references.md) |

---

## The protocol in one breath

```
Layer 0  Plan & scope small     — keep each change small
Layer 1  Automate the obvious   — hooks: lint, format, type, secret-scan
Layer 2  Author self-review     — run it, read your diff, prove it runs, disclose AI
Layer 3  CI safety net          — tests + security scans on every PR
Layer 4  Human review           — correctness → tests → readability → style(last)
Layer 5  Adversarial & PHI pass — attacker check on sensitive data / auth / ML
           → MERGE (approve when it improves code health)
```

**Golden rule:** approve once the change *improves code health* — don't demand perfection.

---

## Why this exists

The hard part of software has shifted from **writing** code to **verifying** it — especially now that AI assistants generate much of it. Research shows AI-generated code carries security flaws in ~45% of cases and developers systematically *over-trust* it. For any team shipping software — and especially when the code handles sensitive data like patient records — review is no longer optional polish; it is a primary safety and compliance control. See [the references](docs/04-references.md) for the evidence.

---

## Who to ask
Maintained by the ACER Research Software Engineering team. Questions, suggestions, and PRs welcome — practice what we preach and open a pull request.

## License

The written materials in this repository are licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE) — you are free to share and adapt them, including for your own team, with attribution to ACER (UIC).
