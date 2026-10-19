# Reviewing AI-Generated Code

Most code at ACER will soon be AI-assisted. That does not lower the review bar - it *raises* it. This doc covers (a) how to write AI code that is reviewable, and (b) how to review it.

**The one principle:** *Treat AI output like a pull request from an eager, fast, over-confident junior developer. It must be verified. Accountability stays with the human - a computer can never be held accountable.*

---

## Part A - Writing AI code that is ready for review

Adapted from Addy Osmani's AI-assisted engineering workflow. These are the author's responsibilities *before* review:

1. **Spec before code.** Describe the problem, constraints, and edge cases first (a short `spec.md`). Do not throw a vague wish at the model.
2. **Small chunks.** Implement one task at a time, test it, commit, move on. Large monolithic AI outputs come back "like 10 devs worked without talking to each other."
3. **Pack context.** Give the model the relevant files, docs, and constraints. Tell it what *not* to do. Less guessing → fewer hallucinations.
4. **Keep a human in the loop.** Read it, run it, test it. "If you have not seen it run, it is not a working system."
5. **Commit often as save points.** Small commits with clear messages = easy rollback when the AI veers off, and a clean history for review.
6. **Use a rules file** (`CLAUDE.md`, `GEMINI.md`, Copilot/Cursor instructions) to encode house style, lint rules, and "ask instead of fabricating." Enforces standards automatically.
7. **Lean on CI/linters/review bots.** Feed failures back to the model; it fixes them. A strong test suite is what lets an agent "fly" safely.

### The AI PR contract (what the author owes the reviewer)
Put this in the PR description:
- **Intent** in 1-2 sentences.
- **Proof it runs**: tests, output, screenshots.
- **AI disclosure**: what the model wrote, and which parts you are least sure about.
- **Where to look**: point the reviewer at the risky areas.
- Confirm you **self-reviewed** first.

---

## Part B - Reviewing AI-generated code

Assume the author may **not fully understand** the diff. Shift your attention:

| De-prioritize (tools handle it) | Prioritize (only a human can) |
|---|---|
| Style, formatting, naming nits | **Intent & understanding**: does this solve the real problem? |
| Lint-level issues | **Correctness at the boundaries**: nulls, empty inputs, error paths |
| | **Security-sensitive paths**: auth, input validation, secrets, injection |
| | **Hallucinated / misused APIs**: does that function/library actually exist and behave as used? |
| | **Design & duplication drift**: AI adds code instead of refactoring; watch for copy-paste |
| | **Proof it was run**: tests and output, not "it compiles" |

### Why the extra scrutiny (the evidence)
- AI code is often **"almost right"**: the hardest kind to catch (66% of devs cite this frustration).
- **~45% of AI-generated code** had security flaws in testing, and newer models were no safer.
- Humans **over-trust** AI: in a controlled study, experienced devs were 19% *slower* with AI but *believed* they were 20% faster. Name this bias and fight it.
- Duplication is rising (~4×) as AI favors adding code over refactoring - maintainability erodes silently.

### AI reviewer tools - what they are, and do we need them?

These are bots that automatically read a pull request and post review comments, like an extra reviewer that is always awake. The common ones:

| Tool | Notes |
|---|---|
| **GitHub Copilot code review** | Built into GitHub/PRs; lowest friction if you are already on GitHub. |
| **CodeRabbit** | Popular standalone PR-review bot; line-by-line comments + summaries. |
| **Graphite (Diamond)** | PR-review bot focused on low false positives. |
| **Cursor / Claude Code** | Can review a diff on request inside your editor. |

- **Good at:** a fast first pass - style nits, obvious bugs, missing tests, common security patterns. Properly tuned, they clear **70-80% of low-hanging fruit** so humans do not waste attention on it.
- **Bad at:** deep domain logic, cross-system design, and *your* project's intent. They also produce **false positives / "text noise"** and can [hallucinate](../GLOSSARY.md#ai-coding-terms).
- **The rule:** use one as a **pre-review gate** that clears noise - then a **human signs off** on logic, security, and architecture. **Augment, never replace.**

**Do we (ACER) need them?** Optional, not required. They are a *nice-to-have*, especially valuable for **solo developers** who have no human reviewer - a bot is a cheap first opinion. They are **not a substitute** for Layers 1-3 (hooks + CI do the deterministic checks more reliably) or for the Layer 4/5 human judgement, and for **PHI code** check the tool's data-handling terms before pointing it at a private health-data repo. Recommendation: **start with pre-commit + CI (free, deterministic). Add GitHub Copilot review or CodeRabbit later if the team wants an extra automated opinion - treat its comments as suggestions, not gospel.**

### The coherence problem (the subtle one)
AI code tends to have **local** correctness but not **global** coherence: overlapping solutions across modules, abstractions that do not compose, naming that drifts. Because each piece looks clean, nothing trips your correction reflex - so the mess accumulates *faster* than with human code. When reviewing, zoom out: does this fit the system, or does it just work in isolation?

### Integration points: where AI is weakest
AI - both as author and as reviewer - is good at the average case and weak at the **edges where code meets something outside the diff**:
- **CI/CD & infrastructure-as-code**: blast radius is underestimated because the diff itself looks small.
- **UI changes**: a tool reads the diff, not the rendered screen; visual regressions are invisible to it.
- **Cross-repo / undocumented conventions**: a change can look fine locally yet violate a convention the tool cannot see.

Give these extra human attention no matter how confident the code or the bot looks.

### Ask the AI to report its deviations
After the AI implements something, ask it: *"Where did you deviate from the plan, and what decisions did you make?"* That surfaces the judgment calls for you to review, instead of making you hunt for surprises in the diff. A short implementation/deviation report is one of the highest-value, lowest-effort review aids - require it in the PR for non-trivial AI work.

### Review happens live, not only at the PR
With an agent, generation already resembles pair programming: the AI is the author, you are the reviewer, in real time. Often the highest-leverage place to apply review skill is **during** generation - steering, correcting, and constraining the agent - not only in an after-the-fact PR. (ACER caveat: live steering does **not** remove the Layer 4/5 pass for anything going to shared, production, or PHI code.)

### Red flags specific to AI output
- A dependency/import you do not recognize → verify it exists and is pinned.
- Overly broad permissions or scopes "to make it work".
- Confident code with no tests.
- Error handling that swallows exceptions silently.
- PHI or secrets in logs, test fixtures, or example data.

See also: the full [references](04-references.md).
