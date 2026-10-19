# The ACER Code Review Protocol
### Condensed deck (10 slides)

> `---` separates slides. ≤5 bullets each. Paste into Marp / reveal.js / Slidev to render. _Italics_ = speaker notes, not for the slide. **[FIGURE]** = suggested visual + where to get it.

---

## Slide 1 — Title

- **Code Review at ACER — A Protocol for the AI Era**
- How we review code, and how to learn it — zero to expert
- Anas Nassar · ACER Research Software Engineering
- Repo: github.com/uicacer/… · October 2026

**[FIGURE]** ACER/UIC logo + a screenshot of a real GitHub pull request.
_Logo: UIC brand portal. PR screenshot: any repo's "Files changed" tab._

---

## Slide 2 — Why now

- The hard part of software shifted: **writing → verifying**
- AI generates code fast — and confidently wrong
- Evidence: **45%** of AI code had security flaws (Veracode); devs **19% slower** with AI but *felt* faster (METR)
- For patient data, a bug = a **HIPAA breach** or a wrong clinical result
- Review is now our main **safety & compliance control**

**[FIGURE]** Three big stat tiles: 45% · 19% · 70%-problem.
_Build as large colored numbers; sources on References slide._

---

## Slide 3 — The model: defense in depth

- Review is a **stack of layers** — each filters noise so the next sees less
- **Cheap & automatic first; scarce human judgement last**
- Layers 1–4 = industry standard
- Layers **0** & **5** = ACER additions (small/solo teams + patient data)
- **Solo mode:** automation carries more of the load

**[FIGURE]** The layered stack diagram (top = cheap/auto, bottom = human). Reuse the ASCII stack from PROTOCOL.md, redrawn.
_Excalidraw: 6 stacked bars, arrow pointing down labeled "less noise each layer."_

---

## Slide 4 — The layers

- **0 · Plan & scope** — small changes (<~400 lines), know what you're building
- **1 · Automate the obvious** — hooks: lint, format, type, secret-scan
- **2 · Author self-review** — run it, read your diff, prove it runs, disclose AI
- **3 · CI safety net** — tests + SAST + dependency scan on every PR
- **4 · Human review** — correctness → tests → readability → style(last)

**[FIGURE]** The same stack as slide 3, with Layer 5 greyed to reveal next slide.

---

## Slide 5 — Layer 5: the ACER addition (patient data)

- Required for **PHI, auth, data access, de-identification, ML, secure compute**
- Put on the **attacker hat**: "how would I *abuse* this?"
- **STRIDE-lite** — 6 yes/no questions (spoof/tamper/repudiate/disclose/DoS/escalate)
- **Blue-team follow-up:** would our logs/alerts catch it? If not → detection gap
- Full red/blue "teaming" is overkill — the **mindset + checklist** is 90% of the value

**[FIGURE]** A split "red hat / blue hat" graphic over a FHIR pipeline icon.
_Icons: thenounproject.com; pipeline = reuse your project's architecture diagram (e.g., AIHealth4All)._

---

## Slide 6 — Solo developer (our reality)

- No peer? You **manufacture** the review signal:
- **Automation** (Layers 1 & 3) = your tireless first reviewer
- **Self-review with distance** — read your own PR the next morning
- **Occasional human** — monthly 30-min with an RSE / US-RSE peer
- **AI reviewer** = fast first opinion, never final sign-off

**[FIGURE]** Hub-and-spoke: one developer in center, 4 "review substitute" arrows in.
_PowerPoint SmartArt radial, or Excalidraw._

---

## Slide 7 — Reviewing AI-generated code

- Treat it like a **junior dev's PR** — must be verified; you stay accountable
- Spend less on style; more on **intent, edge cases, security, hallucinated APIs**
- Require **proof it ran** (tests/output), not "it compiles"
- Watch for: unknown dependencies, widened permissions, no tests, swallowed errors
- **Automation bias is real** — name it, fight it

**[FIGURE]** The "de-prioritize vs prioritize" two-column table.

---

## Slide 8 — Zero-to-expert path

- **L0 Mechanics** — Git, diffs, pull requests (hands-on GitHub Skills)
- **L1 Feedback** — Conventional Comments; give *and* receive well
- **L2 Systematic + automation** — priority-order review; set up hooks + CI
- **L3 Expert** — AI code, adversarial/PHI pass, mentoring
- Everything in the repo, with a plain-language **Glossary**

**[FIGURE]** A 4-step "ascending stairs" graphic (L0→L3).
_PowerPoint SmartArt "ascending steps."_

---

## Slide 9 — What we're adopting

- **Day one (even solo):** pre-commit + CI + self-review + PR template
- **A peer joins:** one required reviewer, rotate, 1-business-day SLA
- **PHI / secure compute:** turn on Layer 5 + security checklist
- **Larger/cross-team:** CODEOWNERS, dual approval; no heavyweight approval boards
- Templates ready to copy: PR template, pre-commit config, CODEOWNERS, checklist

**[FIGURE]** Screenshot of the PR template and `.pre-commit-config.yaml` side by side.

---

## Slide 10 — Takeaways & references

- Review = **verifying**, the core skill now — invest in it
- **Layers:** cheap/automatic first, human judgement last
- **Patient data** earns an adversarial pass; **solo** devs automate + self-review
- Learn it: the repo takes anyone **zero → expert**
- Sources: Google eng-practices · Conventional Comments · Osmani (AI) · OWASP · DORA/Veracode/METR — full list in `docs/04-references.md`

**[FIGURE]** Repo QR code / URL + ACER logo.
