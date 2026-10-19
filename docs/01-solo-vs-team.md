# Solo vs. Team Code Review

Code review assumes a second person. Many ACER projects have exactly one developer. This doc shows how the [protocol](../PROTOCOL.md) works in both cases — and how a solo developer manufactures the "second pair of eyes."

---

## The core difference

| | **Team** | **Solo** |
|---|---|---|
| Who reviews? | A peer | You (with distance) + automation + occasional external |
| Main risk | Bottleneck, bus-factor | No one catches your blind spots |
| What carries the quality | The reviewer | **Automation + disciplined self-review** |
| Approval | Peer approves the PR | You approve after a real self-review pass |

Honest note: some research guidance (Wilson et al., *Good Enough Practices*) **drops** formal review for solo/short-term work. The goal for solo devs is therefore **lightweight substitutes that are worth the effort — not big-team ceremony imposed on one person.**

---

## Team review (2–6 people)

- **One required reviewer per PR** is the sweet spot.
- **Rotate the reviewer role** so knowledge spreads and no one person becomes a bottleneck (fixes bus-factor).
- Keep PRs small; hold the **one-business-day** response norm.
- As the team grows: add `CODEOWNERS` (auto-route to the right approver), explicit review SLAs, and a readability/ownership split. **Avoid central approval boards** — evidence (DORA) shows they make delivery slower *and* less stable.
- **Cross-team changes** (shared libraries, APIs): **dual approval** — the owning team approves the contract/implementation, the consuming team confirms it meets their needs.

## Solo review — the four substitutes

You replace the missing human with four cheap, reliable signals:

### 1. Automation as your first reviewer (the big one)
- **Pre-commit hooks** run formatters, linters, type checks, and **secret scanning** on every commit. See [`templates/.pre-commit-config.yaml`](../templates/.pre-commit-config.yaml).
- **CI (GitHub Actions)** runs your tests on every push/PR. It never gets tired and never skips.
- These two catch the majority of what a human reviewer would flag for style and obvious bugs — automatically.

### 2. Self-review with distance
- **Open a PR to yourself.** Don't merge straight to `main`.
- Review the diff **the next morning**, reading it as if a stranger wrote it.
- Walk the [review checklist](../templates/review-checklist.md) line by line.
- Rubber-duck: explain the change out loud; the bugs surface when you hear yourself.

### 3. An occasional human
- A **monthly 30-minute review** with an ACER RSE, a departmental "code clinic", or a [US-RSE](https://us-rse.org/) peer.
- **Pair or mob** on the tricky parts — Google explicitly counts qualified pair-programming as satisfying review.
- You don't need a human on *every* change — just on the risky ones.

### 4. An AI reviewer as the fast first line
- CodeRabbit / GitHub Copilot review / Cursor can do a 24/7 first pass — nits, obvious bugs, "did you consider…".
- **Never** treat it as sign-off. It hallucinates and misses domain logic. Augment, don't replace. (See [reviewing AI code](02-reviewing-ai-code.md).)

---

## Solo checklist (print this)

Before you merge your own work:
- [ ] Pre-commit + CI are green (tests, lint, secret scan)
- [ ] I opened a PR and read the full diff myself, after a break
- [ ] PR description says what/why/how-to-test
- [ ] I can explain every line — including anything AI wrote
- [ ] No secrets, no PHI in code/logs/tests
- [ ] For sensitive code: I did a 15-min adversary pass ([details](03-adversarial-review.md))
- [ ] Risky changes got a human or AI second opinion
