# Measuring Review Health

Code review culture is fragile. Reviewers are rarely rewarded for depth, and when throughput is the only thing measured, review quietly decays into rubber-stamping. This doc is about keeping review honest: measuring whether it is actually working, without chasing vanity numbers. New terms are in the [Glossary](../GLOSSARY.md).

> This matters more in the AI era, because authoring is now cheap and fast, so review queues grow and the temptation to skim rises.

---

## Signals worth watching

These tell you whether review is flowing and staying real:

- **Time-to-first-approval (P75):** how long a PR waits for its first look. A rising number means the queue is backing up. (One team cut this from about 70h to 44h by [calibrating review depth to risk](../PROTOCOL.md#layer-4--human-review).)
- **Share merged within 24h:** healthy flow for small PRs.
- **The rubber-stamp detector: share of PRs approved within about 1 hour of opening.** A very fast approval is the timing signature of a skim-and-stamp. If this rises as your queue speeds up, attention is dropping. If it falls while throughput improves, reviewers are working smarter, not lazier.
- **Unique human reviewers per PR** and **"changes requested" rate:** if these collapse, review has become a formality.

The goal is not to maximize these numbers. It is to notice when they move in a bad direction.

---

## Beware vanity metrics

Some numbers are easy to collect but do not measure review quality or real risk:

- **Code coverage %.** High coverage can still miss the cases that matter, and low coverage on a critical path is worse than high coverage on trivial code.
- **Linter / Sonar violation counts.** Useful hygiene, but a clean report says nothing about whether the design is right or the change is safe.

Do not let these become the target. They are [vanity metrics](../GLOSSARY.md#review-culture--process-terms): they look like quality but do not guarantee it. Measure attention and outcomes, not digestible proxies.

---

## Deterministic verification shrinks the judgment surface

The more you push into deterministic checks (types, linters, tests, security scanners, i.e. [Layers 1 to 3](../PROTOCOL.md)), the smaller the area left for scarce human judgment. Every category a machine can decide for certain is one less thing a tired human has to catch. So the cheapest way to protect review quality is to invest in automation first, then spend human attention only on what genuinely needs it: correctness, design, security, and PHI.

---

## The author/reviewer imbalance (a real hazard)

In the AI era the effort is lopsided. Generating a large PR is cheap, while reviewing it carefully can take more mental energy than producing it did. Left unmanaged, this creates two failure modes:

1. **The reviewer becomes a bottleneck,** and gets little visible credit while authors claim the delivered features.
2. **"AI PR dumping":** one person generates volume and quietly uses a reviewer as a safety net.

Mitigations ACER should adopt:

- **Authors owe reviewers a reviewable PR:** a small diff, proof it runs, a short AI-deviation note, and the risky parts flagged (the [AI PR contract](02-reviewing-ai-code.md)).
- **Rotate review** so the load and the knowledge spread, with no single safety net.
- **Count review as real work.** It is ownership and knowledge transfer, not a career dead end.
- **Keep changes small** so no single review is overwhelming.

> A note on "reviewer-less" proposals: some argue highly competent engineers should be allowed to ship without review. For throwaway work that may be fine, but for ACER production, shared, or PHI code it is not. The better lesson from that same argument is to move review earlier (review the plan) and keep it live (steer the agent as it generates), not to drop it. See [Reviewing AI code](02-reviewing-ai-code.md).

---

## Solo note
Your signals are simpler, but the spirit is the same. Do not rubber-stamp yourself:

- Did pre-commit and CI stay green on every change?
- Did you actually self-review the diff (after a break), rather than merging within a minute of opening the PR?
- For sensitive changes, did you run the 15-minute [adversary pass](03-adversarial-review.md)?

---

## References
- Nate Goethel (Mews), "Code generation is now cheap, code review still isn't": https://developers.mews.com/code-generation-is-cheap-review-remains-costly/
- Alex Ashitkin, "Code reviews in the AI era": https://medium.com/@xqmbiuy/code-reviews-in-the-ai-era-12698f863924 *(paywalled)*
- More in the full [references](04-references.md).
