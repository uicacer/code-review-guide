# Reviewing AI-Generated Code

Most code at ACER will soon be AI-assisted. That doesn't lower the review bar — it *raises* it. This doc covers (a) how to write AI code that's reviewable, and (b) how to review it.

**The one principle:** *Treat AI output like a pull request from an eager, fast, over-confident junior developer. It must be verified. Accountability stays with the human — a computer can never be held accountable.*

---

## Part A — Writing AI code that's ready for review

Adapted from Addy Osmani's AI-assisted engineering workflow. These are the author's responsibilities *before* review:

1. **Spec before code.** Describe the problem, constraints, and edge cases first (a short `spec.md`). Don't throw a vague wish at the model.
2. **Small chunks.** Implement one task at a time, test it, commit, move on. Large monolithic AI outputs come back "like 10 devs worked without talking to each other."
3. **Pack context.** Give the model the relevant files, docs, and constraints. Tell it what *not* to do. Less guessing → fewer hallucinations.
4. **Keep a human in the loop.** Read it, run it, test it. "If you haven't seen it run, it's not a working system."
5. **Commit often as save points.** Small commits with clear messages = easy rollback when the AI veers off, and a clean history for review.
6. **Use a rules file** (`CLAUDE.md`, `GEMINI.md`, Copilot/Cursor instructions) to encode house style, lint rules, and "ask instead of fabricating." Enforces standards automatically.
7. **Lean on CI/linters/review bots.** Feed failures back to the model; it fixes them. A strong test suite is what lets an agent "fly" safely.

### The AI PR contract (what the author owes the reviewer)
Put this in the PR description:
- **Intent** in 1–2 sentences.
- **Proof it runs** — tests, output, screenshots.
- **AI disclosure** — what the model wrote, and which parts you're least sure about.
- **Where to look** — point the reviewer at the risky areas.
- Confirm you **self-reviewed** first.

---

## Part B — Reviewing AI-generated code

Assume the author may **not fully understand** the diff. Shift your attention:

| De-prioritize (tools handle it) | Prioritize (only a human can) |
|---|---|
| Style, formatting, naming nits | **Intent & understanding** — does this solve the real problem? |
| Lint-level issues | **Correctness at the boundaries** — nulls, empty inputs, error paths |
| | **Security-sensitive paths** — auth, input validation, secrets, injection |
| | **Hallucinated / misused APIs** — does that function/library actually exist and behave as used? |
| | **Design & duplication drift** — AI adds code instead of refactoring; watch for copy-paste |
| | **Proof it was run** — tests and output, not "it compiles" |

### Why the extra scrutiny (the evidence)
- AI code is often **"almost right"** — the hardest kind to catch (66% of devs cite this frustration).
- **~45% of AI-generated code** had security flaws in testing, and newer models were no safer.
- Humans **over-trust** AI: in a controlled study, experienced devs were 19% *slower* with AI but *believed* they were 20% faster. Name this bias and fight it.
- Duplication is rising (~4×) as AI favors adding code over refactoring — maintainability erodes silently.

### AI reviewer tools — what they are, and do we need them?

These are bots that automatically read a pull request and post review comments, like an extra reviewer that's always awake. The common ones:

| Tool | Notes |
|---|---|
| **GitHub Copilot code review** | Built into GitHub/PRs; lowest friction if you're already on GitHub. |
| **CodeRabbit** | Popular standalone PR-review bot; line-by-line comments + summaries. |
| **Graphite (Diamond)** | PR-review bot focused on low false positives. |
| **Cursor / Claude Code** | Can review a diff on request inside your editor. |

- **Good at:** a fast first pass — style nits, obvious bugs, missing tests, common security patterns. Properly tuned, they clear **70–80% of low-hanging fruit** so humans don't waste attention on it.
- **Bad at:** deep domain logic, cross-system design, and *your* project's intent. They also produce **false positives / "text noise"** and can [hallucinate](../GLOSSARY.md#ai-coding-terms).
- **The rule:** use one as a **pre-review gate** that clears noise — then a **human signs off** on logic, security, and architecture. **Augment, never replace.**

**Do we (ACER) need them?** Optional, not required. They're a *nice-to-have*, especially valuable for **solo developers** who have no human reviewer — a bot is a cheap first opinion. They are **not a substitute** for Layers 1–3 (hooks + CI do the deterministic checks more reliably) or for the Layer 4/5 human judgement, and for **PHI code** check the tool's data-handling terms before pointing it at a private health-data repo. Recommendation: **start with pre-commit + CI (free, deterministic). Add GitHub Copilot review or CodeRabbit later if the team wants an extra automated opinion — treat its comments as suggestions, not gospel.**

### Red flags specific to AI output
- A dependency/import you don't recognize → verify it exists and is pinned.
- Overly broad permissions or scopes "to make it work".
- Confident code with no tests.
- Error handling that swallows exceptions silently.
- PHI or secrets in logs, test fixtures, or example data.

See also: the full [references](04-references.md).
