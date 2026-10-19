# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A pure documentation and templates repository — no code, no build system, no tests. All content is Markdown.

- **[PROTOCOL.md](PROTOCOL.md)** — the canonical 6-layer code review workflow (the "standard")
- **[tutorial/](tutorial/)** — 4-level hands-on tutorial (Level 0 mechanics → Level 3 expert/AI)
- **[docs/](docs/)** — deep-dives: solo review, reviewing AI code, adversarial review, references
- **[templates/](templates/)** — reusable artifacts: PR template, review checklist, `.pre-commit-config.yaml`, CODEOWNERS example
- **[GLOSSARY.md](GLOSSARY.md)** — plain-language definitions for every term used in the docs

## Conventions

**Tone and audience:** Written for research software engineers who may be new to code review. Explanations assume the reader knows nothing; every technical term is defined in GLOSSARY.md and cross-linked on first use.

**Cross-linking:** Every doc that introduces a term links to `GLOSSARY.md#anchor`. Every doc links back to PROTOCOL.md and to related tutorial levels. Keep these links alive when editing.

**The 6-layer model** (the organizing principle across all docs):
| Layer | Name | Who/what |
|---|---|---|
| 0 | Plan & scope small | Author |
| 1 | Automate the obvious | Pre-commit hooks |
| 2 | Author self-review | Author |
| 3 | CI safety net | GitHub Actions |
| 4 | Human review | Peer reviewer |
| 5 | Adversarial & PHI pass | Rotating attacker (ACER addition) |

**Solo mode** is a first-class variant: any change to team-mode layers must have a corresponding solo-mode equivalent documented.

**PHI / HIPAA context:** The protocol is general-purpose — it applies to any software project — but gives extra care to sensitive/regulated data (e.g., patient data on AWS HealthLake/FHIR). Security and PHI language in docs/Layer 5 must stay precise (STRIDE-lite, least-privilege, audit logs, synthetic test data).

**Conventional Comments** (`praise:`, `nitpick:`, `suggestion:`, `issue:`, `question:` with `(blocking)`/`(non-blocking)`) are used throughout as the standard for review feedback. References to this convention link to https://conventionalcomments.org/.

## Editing guidance

When adding or revising content, maintain these invariants:
- New terms introduced in any doc must be added to GLOSSARY.md.
- Any new layer-5 requirement must also appear in `templates/review-checklist.md`.
- Tutorial levels must stay sequential; each level references the previous and next.
- The protocol summary table in README.md must stay in sync with PROTOCOL.md.
