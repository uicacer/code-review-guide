# The ACER Code Review Protocol

> **This is our standard.** It's a stack of **layers**. Each layer catches problems so the next layer sees less noise — cheap automated checks first, scarce human judgement last.
>
> **New to the terms** (lint, hook, CI, SAST, PHI, STRIDE…)? Every word is explained in the [**Glossary**](GLOSSARY.md). Never heard of a pull request? Start with the [**tutorial**](tutorial/).

**Golden rule (from Google):** *Approve a change once it improves the overall [code health](GLOSSARY.md#review-culture--process-terms) of the system — don't demand perfection.* Review is for correctness, security, and shared understanding, not personal taste.

---

## The layers at a glance

```
                     ┌─────────────────────────────────────────────┐
  cheap / automatic  │ Layer 0  Plan & scope small                 │
         │           │ Layer 1  Automate the obvious   (hooks)     │
         │           │ Layer 2  Author self-review     (you)       │
         │           │ Layer 3  CI safety net          (every PR)  │
         ▼           │ Layer 4  Human review           (a peer)    │
  scarce / human     │ Layer 5  Adversarial & PHI pass (sensitive) │  ← ACER addition
                     └─────────────────────────────────────────────┘
                              → MERGE (improves code health)
```

**Layers 1–4 are the industry-standard "defense in depth."** Layers **0** and **5** are what we add because ACER keeps small/solo teams and handles **patient data**. A **solo mode** (bottom of this page) tells you what changes when you're the only developer.

---

## Layer 0 — Plan & scope small
*Not a filter — it decides how much work every later layer has to do.*
- Know what you're building **before** you write it. For AI-assisted work, write a short [spec](GLOSSARY.md#ai-coding-terms) first (see [Reviewing AI code](docs/02-reviewing-ai-code.md)).
- **Keep each change under ~400 changed lines.** Small changes get reviewed faster and more thoroughly; big ones hide bugs.
- One logical change per [pull request](GLOSSARY.md#the-basics-git-branches-and-pull-requests). Split unrelated work into separate PRs.

## Layer 1 — Automate the obvious
*Machines catch mechanical problems the instant you commit. No human judgement needed.*
- A [**pre-commit hook**](GLOSSARY.md#automation-the-tools-that-review-code-for-you) runs automatically every time you commit and blocks the commit if a check fails. It runs:
  - a [**linter**](GLOSSARY.md#automation-the-tools-that-review-code-for-you) (flags likely mistakes),
  - a [**formatter**](GLOSSARY.md#automation-the-tools-that-review-code-for-you) (fixes style so nobody argues about it),
  - a [**type checker**](GLOSSARY.md#automation-the-tools-that-review-code-for-you) (catches wrong-data-type bugs),
  - a [**secret scanner**](GLOSSARY.md#security-terms) (blocks passwords/keys from being committed).
- Set-up is one file: [`templates/.pre-commit-config.yaml`](templates/.pre-commit-config.yaml). Learn it in [Tutorial Level 2](tutorial/level-2-systematic.md).

## Layer 2 — Author self-review
*Before you ask anyone (or any tool) to look, you review your own work.*
- **Run the code.** "It compiles" is not proof it works — see it actually run.
- **Read your own [diff](GLOSSARY.md#the-basics-git-branches-and-pull-requests)** line by line, as if a stranger wrote it. Ideally after a short break.
- Optionally get an **AI review in fresh context** (a second AI session that didn't write the code) as a quick first opinion — never as final sign-off.
- **Write a clear PR description:** *what changed, why, how to test, rollback plan.* Use the [PR template](templates/pull_request_template.md).
- **If AI wrote any of it:** say so, and point to the parts you're least sure about. You are accountable for every line regardless of who/what typed it. (The "[AI PR contract](docs/02-reviewing-ai-code.md)".)

## Layer 3 — CI safety net
*An automatic server re-runs everything on every pull request, so nothing slips through because someone forgot.*
- [**CI (Continuous Integration)**](GLOSSARY.md#automation-the-tools-that-review-code-for-you) — e.g., **GitHub Actions** — runs on every PR and reports pass/fail:
  - the full [test suite](GLOSSARY.md#automation-the-tools-that-review-code-for-you),
  - the same lint/format/type checks (in case a hook was skipped),
  - [**SAST**](GLOSSARY.md#security-terms) (scans source code for security holes) and [**dependency scanning**](GLOSSARY.md#security-terms) (checks your libraries for known vulnerabilities),
  - secret scanning again, on the whole history.
- A red (failing) CI check means **no human review yet** — fix CI first.

## Layer 4 — Human review
*Now a person spends their scarce attention only on what machines can't judge.* Review in **priority order** — don't sweat the small stuff until the big stuff is clear:
1. **Correctness & design** — does it do the right thing? Does it fit the architecture?
2. **Tests** — do they exist and cover the new logic and edge cases?
3. **Readability & naming** — will someone understand this in six months?
4. **Style** — *last*, and automated so humans never argue about it.

Rules of the human pass:
- **Respond within one business day.** Slow reviews block the author more than they help.
- **Use [Conventional Comments](https://conventionalcomments.org/):** prefix every comment — `praise:`, `nitpick:`, `suggestion:`, `issue:`, `question:` — and mark `(blocking)` vs `(non-blocking)`. Learn this in [Tutorial Level 1](tutorial/level-1-feedback.md).
- Comment on the code, not the person. Explain *why*. Ask, don't command.

---

## Layer 5 — Adversarial & PHI pass  *(ACER addition — sensitive code only)*

**Required** for any change touching **sensitive or regulated data (e.g., patient data/PHI), authentication, data access, de-identification, a secure compute environment, or ML inputs/outputs** — common in ACER projects such as AIHealth4All. Full walkthrough with plain-language explanations: [Adversarial review](docs/03-adversarial-review.md).

This layer adds the **attacker's point of view** on top of normal review:
- One reviewer (rotating weekly) puts on the [**attacker hat**](GLOSSARY.md#the-adversarial-redblue-team-terms): instead of "does this work?", they ask **"how would I abuse this?"** This is [**adversarial review**](GLOSSARY.md#the-adversarial-redblue-team-terms).
- They run the [**STRIDE-lite**](GLOSSARY.md#the-adversarial-redblue-team-terms) checklist — six yes/no questions, one per threat type (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).
- **PHI questions:** Is any patient data exposed in logs, errors, URLs, or test data? Is access [least-privilege](GLOSSARY.md#security-terms)? Is data encrypted [at rest and in transit](GLOSSARY.md#security-terms)? Are [audit logs](GLOSSARY.md#security-terms) on?
- **Defender follow-up (the "blue team" half):** for each risk found, ask *"would our logs/alerts catch it if it happened?"* If not, write it down as a detection gap.
- Use the [security & PHI checklist](templates/review-checklist.md).

> **Why we add this:** a normal review asks if the code is correct. For patient data, a bug isn't just wrong — it can be a reportable **HIPAA** breach or a harmful clinical result. The attacker lens catches a different, higher-stakes class of problem. See [why red/blue teaming, right-sized](docs/03-adversarial-review.md).

---

## Merge
- Author resolves every `(blocking)` comment (discuss, don't silently ignore).
- Receive feedback gracefully: fix the code, don't defend ego. Disagree productively; escalate if truly stuck.
- Reviewer **approves once the change improves code health** — not once it's flawless.
- **Squash merge** with a clear message; delete the branch.
- **Monitor** for ~30 minutes after any production deploy.

---

## Solo mode — when you're the only developer

Most ACER projects have one developer and no one to be the Layer 4 "peer." You don't skip review — you **manufacture** it. What changes:

| Layer | Team | **Solo** |
|---|---|---|
| 0 Plan & scope | same | same |
| 1 Hooks | same | **same — your most important safety net** |
| 2 Self-review | same | **same — do it seriously, with a delay** |
| 3 CI | same | **same — it's your tireless reviewer** |
| 4 Human review | a peer approves | **you review your own PR the next morning, by checklist; + a monthly 30-min review with an ACER RSE / peer / [US-RSE](https://us-rse.org/); + optional AI reviewer as a first opinion** |
| 5 Adversarial | rotating adversary | **a timed 15-minute attacker pass on your own diff, out loud** |

Honest note: for tiny, throwaway solo scripts, full process is overkill — lean on Layers 1–3 and a quick self-review. Scale up as the code gets closer to real patient data or production. Full detail: [Solo vs team](docs/01-solo-vs-team.md).

---

## Adoption ladder — start light, grow with the team
1. **Day one (even solo):** Layers 0–3 — pre-commit + CI + self-review, PR template in use.
2. **A second person joins:** add Layer 4 — one required reviewer per PR, rotate the role, one-business-day response.
3. **Code touches PHI / secure compute:** turn on Layer 5 — adversarial pass + security checklist.
4. **Larger / cross-team:** add [`CODEOWNERS`](GLOSSARY.md#review-culture--process-terms), required reviews, and dual approval across team boundaries. Avoid heavyweight central approval boards — evidence shows they make delivery slower *and* less stable.

See the full [references](docs/04-references.md).
