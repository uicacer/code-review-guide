# Code Review: A Practical Guide
### Slide outline (draft for building a Google Slides deck)

> One slide per `---`. Max 5 bullets per slide. _Italics_ are speaker notes. **[FIGURE]** marks a suggested visual.

---

## Slide 1: Title

- Code Review: A Practical Guide
- A layered standard for reviewing code, from basics to expert
- Special care for AI-generated code and sensitive data
- Full guide and templates: https://github.com/uicacer/code-review-guide

**[FIGURE]** Screenshot of a real pull request with review comments.

---

## Slide 2: Why this matters now

- AI writes code fast, but ~45% of it has security flaws ([Veracode 2025](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/))
- The "70% problem" ([Osmani](https://addyo.substack.com/p/the-70-problem-hard-truths-about)): AI gets you 70% quickly; the critical last 30% still needs human judgment
- For sensitive data, a missed bug is not just wrong; it can be a reportable breach or wrong clinical result
- Review is the primary quality and safety control now, not optional polish

**[FIGURE]** Two stat tiles: 45% · 70%.

---

## Slide 3: The protocol, six layers

- **Golden rule** ([Google](https://google.github.io/eng-practices/review/reviewer/standard.html)): approve once it improves code health (overall quality); do not demand perfection
- **Defense in depth**: stack independent layers so if one fails the next catches it; cheap and automatic first, human judgment last
- **Layers 0-3**: plan small, pre-commit hooks (auto-checks before each commit), self-review, CI (server that reruns all checks on every PR)
- **Layer 4**, Human review: correctness, design, tests; calibrate depth to blast radius (how much damage a bug here causes)
- **Layer 5**, Adversarial pass: required for sensitive data, auth, or ML (next slide)

_Layers 0-4 are industry-standard. Layer 5 is added specifically for sensitive or patient data._

**[FIGURE]** Six stacked bars: top = cheap/automatic, bottom = human.

---

## Slide 4: Layer 5, the sensitive-data pass

- Required for PHI (patient data), authentication, de-identification (removing patient identifiers), ML inputs/outputs
- Attacker mindset: "how would someone abuse this?" instead of "does this work?"
- [STRIDE-lite](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats): six yes/no questions: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- For ML: also check model poisoning (corrupting training data), membership inference (recovering patient identity from a model), adversarial inputs (crafted inputs that fool the model)
- Defender follow-up: would our logs catch it? If not, file a detection gap

**[FIGURE]** Red hat (attacker) + blue hat (defender) over a data-pipeline icon.

---

## Slide 5: Reviewing AI-generated code

- Treat it like a confident junior developer: verify intent, edge cases, security, and hallucinated APIs (functions the AI invented that do not exist)
- Coherence problem: each piece looks clean, but the design drifts across the whole; review by logical unit, not line by line
- Review live too: steer the AI agent (a tool that writes code autonomously) during generation, not only at the PR
- AI PR contract: author states intent, shows proof it ran, discloses what the AI wrote, and flags uncertain parts
- Human accountability: no AI output takes effect without a named human sign-off

**[FIGURE]** Two columns: "spend less on" (style, formatting) vs "spend more on" (intent, security, hallucinated APIs).

---

## Slide 6: Solo and how to adopt

- Solo mode: automation (hooks + CI) + self-review next morning + monthly peer + AI review bot (strongly recommended; check data terms for PHI repos)
- Day one, even solo: hooks, CI, self-review, PR template; add Layer 5 when code touches sensitive data
- Second developer joins: one required reviewer per PR, rotate the role, one-business-day response
- Health signal: high rate of approvals within one hour = rubber-stamping (approving without actually reviewing) ([Goethel, Mews](https://developers.mews.com/code-generation-is-cheap-review-remains-costly/))
- Tutorial: four levels (L0 mechanics to L3 AI and adversarial): https://github.com/uicacer/code-review-guide

**[FIGURE]** Maturity ladder: Solo, Small team, Larger team.

---

## Slide 7: Takeaways

- Review is the core skill now; verifying code matters more than writing it
- Cheap and automatic first; human judgment last; golden rule: approve once it improves code health
- Sensitive data always earns an adversarial pass; ML adds model poisoning and membership inference checks
- AI code: trust but verify; review live, require proof it ran, hold the human accountable
- Full guide, templates, and tutorial: https://github.com/uicacer/code-review-guide

**[FIGURE]** QR code linking to https://github.com/uicacer/code-review-guide.
