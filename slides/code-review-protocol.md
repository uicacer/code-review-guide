# Code Review: A Practical Guide
### Slide outline (draft for building a Google Slides deck)

> One slide per `---`. Keep each slide to 5 short bullets maximum. _Italics_ are speaker notes, not for the slide. **[FIGURE]** marks a suggested visual and where to get it. Plain prose style: no em dashes, no contractions.

---

## Slide 1: Title

- Code Review: A Practical Guide
- A layered standard for reviewing code well, from zero to expert
- Special care for AI-generated code and sensitive or patient data
- Full guide and templates: https://github.com/uicacer/code-review-guide
- Presenter name, affiliation, date

**[FIGURE]** A clean title graphic, or a screenshot of a real pull request.

---

## Slide 2: Why this matters now

- The hard part of software shifted from writing code to verifying it
- The "70% problem" ([Osmani](https://addyo.substack.com/p/the-70-problem-hard-truths-about)): AI tools reach 70% of a solution quickly and confidently; the critical last 30% requires human judgment — that gap is exactly what review catches
- Evidence: ~45% of AI code had security flaws ([Veracode 2025](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)); developers were 19% slower with AI but felt faster ([METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/))
- For sensitive data, a defect is not just a bug — it can be a breach (unauthorized exposure) or a wrong clinical result
- Review is no longer optional polish; it is a primary safety and quality control

**[FIGURE]** Three large stat tiles: 45%, 19%, 70%. _Build as big colored numbers._

---

## Slide 3: The protocol — six layers of defense

- **Golden rule** ([Google eng-practices](https://google.github.io/eng-practices/review/reviewer/standard.html)): approve a change once it improves code health (the overall quality and correctness of the codebase); do not demand perfection
- Defense in depth: multiple independent layers so if one fails the next catches it — cheap and automatic first, scarce human judgment last
- Layers 0-3: plan small; pre-commit hooks (scripts that run automatically before each commit); self-review; CI (Continuous Integration — a server that reruns all checks on every pull request)
- Layer 4, Human review: correctness, design, and alignment; then tests; readability; style last — calibrate depth to blast radius (how much damage a bug here would cause)
- Layer 5, Adversarial pass: required for sensitive data, authentication, or ML — next slide

_Layers 0-4 are all industry-standard good practice. Layer 5 is added specifically for sensitive or patient data._

**[FIGURE]** Six stacked bars: top = cheap/automatic, bottom = human, arrow "less noise each layer." _Excalidraw._

---

## Slide 4: Layer 5 — the sensitive-data pass

- Required for PHI (Protected Health Information — patient data), authentication, data access, de-identification (removing patient identifiers from data), ML, secure compute
- Put on the attacker hat: how would someone abuse this?
- [STRIDE-lite](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats): six yes or no questions (spoof, tamper, repudiate, disclose, deny, escalate)
- For ML components, STRIDE alone is not enough — also check: model poisoning (corrupting training data to skew outputs), membership inference (recovering patient identities from a trained model), adversarial inputs (crafted inputs that cause incorrect model behavior)
- Defender follow-up: would our logs or alerts catch it? If not, file a detection gap (a risk your monitoring would not catch)

**[FIGURE]** A red-hat and blue-hat split over a data-pipeline icon. _Icons: thenounproject.com._

---

## Slide 5: Reviewing AI-generated code

- Treat it like a confident junior developer: verify intent, edge cases, security, and hallucinated APIs (functions or libraries the AI invented that do not actually exist) — not just style
- The coherence problem: review by logical unit, not line order — each piece looks clean but the design drifts across the whole
- Review happens live too: steer the AI agent (a tool that writes code autonomously) as it generates; the highest-leverage moment is often during generation, not only at the pull request
- The AI PR contract: author states intent, shows proof it ran, asks the AI where it deviated from the plan, and discloses which parts they are least sure about
- Human accountability: no AI output takes effect without a named human gate — the author is responsible for every line

**[FIGURE]** Left: spend less on (style, formatting). Right: spend more on (intent, edge cases, security, hallucinated APIs, proof it ran).

---

## Slide 6: Solo and how to adopt

- Solo: manufacture review from four sources — automation (hooks + CI), self-review the next morning by checklist, monthly peer, AI review tool (strongly recommended when no human peer is available; check data-handling terms for PHI — patient data — repositories)
- Day one (even solo): hooks, CI, self-review, a pull-request template; add Layer 5 when code touches sensitive data
- A second person joins: one required reviewer, rotate the role, one-business-day response; larger teams add CODEOWNERS (a file that auto-assigns reviewers by which files changed) and dual approval ([DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report))
- Health check: watch time to first approval; a high rate of approvals within one hour signals rubber-stamping (approving without actually reviewing) ([Goethel, Mews](https://developers.mews.com/code-generation-is-cheap-review-remains-costly/))
- Learn it: four tutorial levels (L0: mechanics to L3: AI and adversarial review), each with hands-on exercises — https://github.com/uicacer/code-review-guide

**[FIGURE]** A maturity ladder: Solo, Small, Large.

---

## Slide 7: Takeaways

- Review is about verifying; it is the core skill now — invest in it
- Layers: cheap and automatic first, human judgment last; golden rule: approve once it improves code health ([Google](https://google.github.io/eng-practices/review/reviewer/standard.html))
- Sensitive data earns an adversarial pass; for ML add the AI/ML threat angle alongside STRIDE
- For AI code: trust but verify, review live, require proof it ran, hold the human accountable
- Augment with AI tools, never replace the human — full guide: https://github.com/uicacer/code-review-guide

**[FIGURE]** QR code linking to https://github.com/uicacer/code-review-guide. _Full annotated references: docs/04-references.md._
