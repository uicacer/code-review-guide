# Code Review Guide For ACER
### Slide outline — mirrors the current Code_Review_Guide.pptx

> One slide per `---`. Build animations are shown as the final revealed state. _Italics_ are speaker notes. **[FIGURE]** marks a suggested visual.

---

## Slide 1: Title

- Code Review Guide For ACER
- Anas Nassar, Research Software Engineer
- nassar@uic.edu
- https://github.com/uicacer/code-review-guide

---

## Slide 2: Why this matters now

- The hard part of software shifted from writing code to verifying it
- AI writes code fast, but ~45% of it has security flaws ([Veracode 2025](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/))
- The "70% problem" ([Osmani](https://addyo.substack.com/p/the-70-problem-hard-truths-about)): AI gets you 70% quickly; the critical last 30% still needs human judgment
- For sensitive data, a missed bug is not just wrong; it can be a reportable breach or wrong clinical result

**[FIGURE]** Two stat tiles: 45% · 70%.

---

## Slide 3: The protocol, six layers of defense

- **L0  Plan and scope**: keep changes small; review the plan before generating code
- **L1  Automate the obvious**: hooks (scripts that run before each commit) run lint, format, type check, secret scan
- **L2  Author self-review**: run it, read your diff as a stranger, disclose AI use
- **L3  CI safety net** (Continuous Integration, a server that reruns all checks on every pull request): full test suite and security scans on every PR
- **L4  Human review**: correctness, design, alignment; then tests, readability, style
- **L5  Sensitive-data pass**: adversarial pass for sensitive data, auth, or ML

_Golden rule ([Google eng-practices](https://google.github.io/eng-practices/review/reviewer/standard.html)): approve a change once it improves code health (overall quality and correctness); do not demand perfection._

**[FIGURE]** Six stacked bars building one at a time; golden rule pinned at the bottom.

---

## Slide 4: Layer 5, the sensitive-data pass

- **Required for**: patient data (PHI), auth, data access, de-identification (removing patient identifiers), ML, secure compute
- **Attacker hat**: STRIDE-lite, a lightweight version of full threat modeling reduced to six yes/no questions any reviewer can answer

| Threat | Question |
|---|---|
| Spoof | Can someone pose as another user? |
| Tamper | Can data change undetected? |
| Repudiate | Can actions be denied later? |
| Disclose | Can data reach the wrong person? |
| Deny | Can the service be knocked out? |
| Escalate | Can a user gain extra rights? |

- **For ML components**: also check model poisoning (corrupting training data to skew outputs), membership inference (recovering patient identity from a trained model), adversarial inputs (crafted inputs that fool the model)
- **Defender follow-up**: would our logs or alerts catch it? If not, file a detection gap (a risk your monitoring would not catch)

**[FIGURE]** Red hat (attacker) + blue hat (defender) over a data-pipeline icon.

---

## Slide 5: Human review, calibrate to risk and label clearly

- **Calibrate depth to blast radius** (how much damage a bug here would cause)
  - Low risk (docs, tests, isolated helpers): conceptual review is enough
  - High risk (shared code, migrations, auth, APIs, infrastructure): line by line
- **Sensitive data is always high risk**, whatever the tier
- **Label every comment** using [Conventional Comments](https://conventionalcomments.org/): `issue (blocking):`, `suggestion (non-blocking):`, `praise:`, `question:`, `nitpick:`
- Example: `issue (blocking): Token logged in plain text`

**[FIGURE]** Risk matrix: low vs high, with a hard floor for sensitive data.

---

## Slide 6: Reviewing AI-generated code

- Treat it like a confident junior developer's work: fast, over-confident, must be verified

| Spend less on | Spend more on |
|---|---|
| Style, formatting, naming nits | Intent and understanding |
| | Edge cases and error paths |
| | Security-sensitive paths |
| | Hallucinated APIs (functions the AI invented that do not exist) |

- **Review by logical unit, not line order**: each piece looks clean while the design drifts across the whole
- **Steer the agent** (a tool that writes code autonomously) while it generates; often the highest-leverage moment, before the PR
- **Require proof it ran**: tests, output, screenshots; "it compiles" is not enough

**[FIGURE]** Two columns: spend less vs spend more, with icons.

---

## Slide 7: The AI pull request contract

- **Human accountability**: no AI output takes effect without a named human gate; the author is responsible for every line

Pull request description checklist:
- Proof it runs: tests, output, screenshots
- AI disclosure: what the AI wrote and where you are least sure
- Intent: what the change does and why
- Where to look: point the reviewer at the risky areas

---

## Slide 8: Adopt it and keep it honest

- **Solo**: hooks, CI, self-review, PR template; add Layer 5 when code touches sensitive data
- **Small team**: one required reviewer, rotate the role, one-business-day response
- **Large team**: CODEOWNERS (a file that auto-assigns reviewers by which files changed) and dual approval; no heavyweight central approval boards
- **Sensitive data at any size**: turn on Layer 5
- **Health check**: a high rate of approvals within one hour signals rubber-stamping (approving without actually reviewing)

**[FIGURE]** Maturity ladder: Solo, Small team, Large team.

---

## Slide 9: Takeaways

- **Verify**: review is the core skill now; invest in it
- **Layer**: cheap and automatic first, human judgment last; approve once code health improves
- **Protect**: sensitive data earns an adversarial pass; solo developers automate and self-review with discipline
- **AI code**: trust but verify, review live, require proof it ran, hold the human accountable
- **Augment**: use AI tools to help review, never to replace the human

---

## Slide 10: Thank you

- Questions?
- https://github.com/uicacer/code-review-guide
