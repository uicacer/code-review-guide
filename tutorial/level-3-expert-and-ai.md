# Level 3 - Expert: AI Code & Adversarial Review

**Goal:** handle the two hardest, highest-stakes cases - reviewing **AI-generated code**, and doing a security/PHI **adversarial pass** (Layer 5) - and start mentoring others.

> Prerequisite: [Levels 0-2](level-0-mechanics.md). All terms in the [Glossary](../GLOSSARY.md).

---

## Part A - Reviewing AI-generated code

Most code at ACER will soon be written with an [AI coding assistant](../GLOSSARY.md#ai-coding-terms) (Copilot, Claude, Cursor, Gemini). This does **not** lower the review bar - it raises it.

**The one principle:** *Treat AI output like a pull request from an eager, fast, over-confident junior developer. It must be verified. You are accountable for every line - a computer cannot be held accountable.*

### Why AI code needs extra scrutiny (the evidence)
- It is often **"[almost right](../GLOSSARY.md#ai-coding-terms)"**: looks clean, reads well, but is subtly wrong. The hardest kind to catch.
- **~45%** of AI-generated code had security flaws in large-scale testing; newer models were no safer.
- [**Automation bias**](../GLOSSARY.md#ai-coding-terms): in a controlled study, experienced developers were *19% slower* with AI but *believed* they were *20% faster*. We systematically over-trust it.
- The "[70% problem](../GLOSSARY.md#ai-coding-terms)": AI nails the first 70%; the last 30% (edge cases, correctness, fit) is exactly where review earns its keep.

### What to focus on (vs human code)
Assume the author may not fully understand the diff. So:

| Spend LESS time on (tools handle it) | Spend MORE time on (only a human can) |
|---|---|
| Style, naming, formatting | **Intent**: does it solve the *real* problem? |
| Lint-level issues | **Edge cases**: empty input, nulls, error paths |
| | **Security paths**: auth, input validation, [secrets](../GLOSSARY.md#security-terms), [injection](../GLOSSARY.md#security-terms) |
| | [**Hallucinated**](../GLOSSARY.md#ai-coding-terms) **APIs**: does that function/library actually exist? |
| | **Duplication**: AI adds code instead of reusing; watch for copy-paste |
| | **Proof it ran**: tests and output, not "it compiles" |

### AI red flags
- An import/dependency you do not recognize → confirm it exists and is pinned to a version.
- Permissions or scopes widened "to make it work."
- Confident code with **no tests**.
- Error handling that silently swallows failures.
- [PHI](../GLOSSARY.md#health-data-terms) or secrets in logs, test data, or examples.

### AI *reviewer* tools (CodeRabbit, Copilot review)
Use them as a **fast first pass** that clears 70-80% of low-hanging fruit - then a human signs off on logic, security, and design. **Augment, never replace.** Full detail: [Reviewing AI code](../docs/02-reviewing-ai-code.md).

### Hands-on
- Read Addy Osmani's "**The 70% Problem**" - https://addyo.substack.com/p/the-70-problem-hard-truths-about
- Take an AI-generated PR, find the hidden bug, and **add the missing test.**

---

## Part B - Adversarial & PHI review (Layer 5)

For any code touching **patient data, authentication, data access, de-identification, a secure compute environment, or ML inputs/outputs.** Plain-language deep dive: [Adversarial review](../docs/03-adversarial-review.md).

### What "adversarial" means
Normal review asks *"does this work?"* [**Adversarial review**](../GLOSSARY.md#the-adversarial-redblue-team-terms) asks *"how would someone **abuse** this?"* You deliberately put on the [**attacker hat**](../GLOSSARY.md#the-adversarial-redblue-team-terms) - think like a hacker for a few minutes - because builders and attackers notice different things.

### STRIDE-lite - a beginner's security checklist
[**STRIDE**](../GLOSSARY.md#the-adversarial-redblue-team-terms) is six categories of threat. Ask one yes/no question per letter:
- **S**poofing - could someone pretend to be another user/service here?
- **T**ampering - could someone change data they should not?
- **R**epudiation - if someone did something bad, would we have a log proving it?
- **I**nformation disclosure - could this leak [PHI](../GLOSSARY.md#health-data-terms) (in logs, errors, URLs, test data)?
- **D**enial of service - could someone overwhelm or crash this?
- **E**levation of privilege - could someone gain more access than intended?

### Red vs blue, in one line each
- [**Red team**](../GLOSSARY.md#the-adversarial-redblue-team-terms) (attacker): *find the hole.*
- [**Blue team**](../GLOSSARY.md#the-adversarial-redblue-team-terms) (defender): *for each hole, would our logs/alerts catch it?* If not → detection gap.
- Doing both in a loop is a miniature [**purple team**](../GLOSSARY.md#the-adversarial-redblue-team-terms) - and that is all the "red/blue teaming" a research group needs.

### Hands-on
- Read [docs/03-adversarial-review.md](../docs/03-adversarial-review.md) and the [review checklist](../templates/review-checklist.md).
- Take a PR that touches data access and run the STRIDE-lite six questions on it out loud.

---

## Part C - Becoming a mentor (true expert level)

- **You learn review by doing review**: volume builds judgement. Review often.
- **Shadow then be shadowed:** pair-review with a newcomer, then have them review and you review *their review*.
- **Handle disagreement well**: see Google's "[pushback](https://google.github.io/eng-practices/review/reviewer/pushback.html)". Stay anchored to code health, not ego.
- **Grow the team's floor:** be (or appoint) a [security champion](../GLOSSARY.md#the-adversarial-redblue-team-terms) who owns the PHI checklist and teaches it.

---

## Level 3 deliverable
- [ ] Reviewed an AI-generated PR: found a correctness/security issue and added a test.
- [ ] Ran a STRIDE-lite adversarial pass on a data-touching PR and filed any detection gaps.
- [ ] Pair-reviewed with another developer.

🎓 **You can now carry out every layer of the [ACER Code Review Protocol](../PROTOCOL.md).**

---

## Solo note
Alone, you play both red and blue on your own diff: a timed **15-minute attacker pass** out loud, then the defender question for anything you find. For AI code, use a *second, fresh* AI session to critique what the first one wrote - a cheap independent opinion, never a substitute for your own judgement.
