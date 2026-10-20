# Level 2 - Systematic Review & Automation

**Goal:** (a) run a full human review in a repeatable order, and (b) set up the machines that do the boring checks for you - so you (and reviewers) only spend attention where it matters. This is Layers 1-4 of the [protocol](../PROTOCOL.md).

> Prerequisite: [Levels 0-1](level-0-mechanics.md). All terms in the [Glossary](../GLOSSARY.md).
> Practice it: [exercises/level-2-review](../exercises/level-2-review/).

---

## Part A - The automation, explained from scratch

The single biggest upgrade to your code quality is letting software catch routine problems automatically. Here is what each tool is, in plain words, and why you want it.

### What is a "linter"?
A [**linter**](../GLOSSARY.md#automation-the-tools-that-review-code-for-you) reads your code and flags likely mistakes **without running it**: unused variables, undefined names, suspicious patterns. It is **spell-check for code**.
- Python: `ruff` (fast, modern) or `flake8`. JavaScript: `eslint`.
- Example: it warns you that `resutl` was never defined (you typo'd `result`).

### What is a "formatter"?
A [**formatter**](../GLOSSARY.md#automation-the-tools-that-review-code-for-you) automatically rewrites your code into one consistent style - indentation, quotes, line length. It means **no human ever argues about layout in review again.**
- Python: `black`. JavaScript/web: `prettier`.

### What is a "type checker"?
A [**type checker**](../GLOSSARY.md#automation-the-tools-that-review-code-for-you) catches bugs where you use the wrong *kind* of data - e.g., treating text as a number - before the code runs.
- Python: `mypy`.

### What is a "hook"?
A [**Git hook**](../GLOSSARY.md#automation-the-tools-that-review-code-for-you) is a script Git runs **automatically at a specific moment**. The one we care about is the **pre-commit hook**: it runs *right before a commit is saved*, and if a check fails, it **stops the commit** until you fix the problem. So bad code never even enters history.
- The tool that manages this easily is called [**pre-commit**](https://pre-commit.com/). You list your checks in one file, [`.pre-commit-config.yaml`](../templates/.pre-commit-config.yaml), and run `pre-commit install` once.

### What is a "secret scan"?
A [**secret**](../GLOSSARY.md#security-terms) is a password, API key, or token that must stay private. A [**secret scanner**](../GLOSSARY.md#security-terms) searches your code for these and **blocks them from being committed**: because once a secret is pushed to GitHub, you must assume it is compromised.
- Tools: `gitleaks`, `TruffleHog`, and GitHub's built-in secret scanning.

### What is "SAST"?
[**SAST**](../GLOSSARY.md#security-terms) = **Static Application Security Testing**. "Static" means it reads your source code without running it; it looks for *security* holes specifically - like [injection](../GLOSSARY.md#security-terms) or unsafe input handling. It is a linter focused on security.
- Tools: CodeQL (free on GitHub), Semgrep, Bandit (Python).

### What is "CI"?
[**CI (Continuous Integration)**](../GLOSSARY.md#automation-the-tools-that-review-code-for-you) is a service that **automatically runs all your checks on a server every time you push or open a PR**, and shows a green ✔ or red ✘ on the PR. On GitHub it is **GitHub Actions**, configured by a small file in `.github/workflows/`.
- Think of CI as a **tireless reviewer** that never forgets to run the tests and never skips a step.
- CI is a general concept, not a single product. GitHub Actions is one implementation; GitLab CI/CD, Bitbucket Pipelines, CircleCI, and Jenkins are others. The same principle applies everywhere, so if your project lives elsewhere the ideas below transfer - only the config file's name and syntax change. We use GitHub Actions for the hands-on because it is the most common for research code.

### What about "CD"?
You will often see "CI/CD" written together. **CD** ([Continuous Delivery / Deployment](../GLOSSARY.md#automation-the-tools-that-review-code-for-you)) is the step *after* CI: once the checks pass, it automatically ships the code to a staging or production environment. For code review, CI is the part that matters, because it decides whether a change is safe to accept. CD is simply where an approved change goes next, so we mention it only to place CI in context.

### How they fit the layers
```
Layer 1 (on your laptop, every commit):   pre-commit hook → lint + format + type + secret scan
Layer 3 (on the server, every PR):        CI (GitHub Actions) → tests + lint + SAST + dependency + secret scan
```
Layer 1 gives instant feedback; Layer 3 is the backstop in case a hook was skipped.

### Hands-on: set up your automated reviewer (~60 min)
1. Copy [`templates/.pre-commit-config.yaml`](../templates/.pre-commit-config.yaml) into a repo, then run:
   ```bash
   pip install pre-commit
   pre-commit install
   pre-commit run --all-files
   ```
   Now every `git commit` auto-runs your checks.
2. Copy [`templates/github-actions-ci.yml`](../templates/github-actions-ci.yml) into your repo at `.github/workflows/ci.yml`. It runs your pre-commit checks and tests on every push and PR. To understand how it works, read **Understanding GitHub Actions**: https://docs.github.com/en/actions/about-github-actions/understanding-github-actions
3. For research-specific setup, read The Turing Way on CI - https://book.the-turing-way.org/reproducible-research/ci

---

## Part B - The human review, done systematically

When the machines are green, a human looks at what machines *cannot* judge. Go in **priority order** (from Google's "[How to do a code review](https://google.github.io/eng-practices/review/reviewer/)") and do not get stuck on trivia before the big things are settled:

1. **Correctness & design**: Does it actually solve the problem? Does it fit the existing architecture, or fight it?
2. **Tests**: Are there tests? Do they cover the new logic *and* the edge cases (empty input, errors, boundaries)?
3. **Readability & naming**: Will a stranger (or future-you) understand this in six months? Are names clear?
4. **Style**: *Last*, and already handled by the formatter - so you should not be commenting on it at all.

Two rules that keep review healthy:
- **Speed:** respond within **one business day**. Review latency, not reviewer effort, is what slows a team ([Google on speed](https://google.github.io/eng-practices/review/reviewer/speed.html)).
- **The bar:** **approve when the change improves [code health](../GLOSSARY.md#review-culture--process-terms)**: not when it is perfect ([the Standard](https://google.github.io/eng-practices/review/reviewer/standard.html)).

Use the [review checklist](../templates/review-checklist.md) until the order is second nature.

### Keep changes small
You can only review ~200-400 changed lines well in one sitting (~60 minutes). If a PR is bigger, ask the author to split it. Small PRs are the single highest-leverage habit for good review.

---

## Level 2 deliverable
- [ ] A repo with a working `.pre-commit-config.yaml` (hooks run on commit).
- [ ] A CI workflow that runs tests on every PR (green check visible).
- [ ] One human review done in priority order, using the checklist.

---

## Solo note
This level **is** your reviewer when you work alone. Pre-commit (Layer 1) + CI (Layer 3) catch most mechanical and security issues automatically, and the priority-ordered self-review (do it the next morning) covers the human judgement. Set these up once and they protect every future commit.

---

**Next:** [Level 3 - Expert: AI code & adversarial review →](level-3-expert-and-ai.md)
