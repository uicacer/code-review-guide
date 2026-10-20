# Glossary - Plain-Language Definitions

Every term we use, explained simply. No prior knowledge assumed. If a doc uses a word you do not know, it is here.

> Format: **Term**: what it is, in plain words. *Why it matters for review.*

---

## The basics: Git, branches, and pull requests

**Version control**: A system that records every change to your code over time, so you can see what changed, who changed it, and go back to any earlier version. Like "track changes" in Word, but for code and far more powerful. The standard tool is **Git**.

**Git**: The program that does version control on your computer. You "commit" changes to it.

**Repository ("repo")**: A project folder that Git is tracking. It holds your code *and* the full history of every change. Can live on your laptop and/or on a website like GitHub.

**GitHub**: A website that hosts Git repositories online so people can share code and review each other's changes. (GitLab and Bitbucket are alternatives.)

**Commit**: A single saved snapshot of your changes, with a short message describing what you did (e.g., "Fix date parsing bug"). Think of it as a save point in a video game.

**Branch**: A parallel copy of the code where you can work without disturbing the main version. You make a branch, do your work, then merge it back. The primary branch is usually called **`main`**.

**Push / Pull**: *Push* = upload your commits from your laptop to GitHub. *Pull* = download the latest commits from GitHub to your laptop.

**Clone**: Make a local copy of a repository from GitHub onto your computer.

**Diff**: The list of exact lines that changed: additions (usually green, with `+`) and deletions (usually red, with `-`). When you review code, you are mostly reading a diff. *This is the core thing a reviewer looks at.*

**Pull Request ("PR") / Merge Request**: A formal request to merge your branch's changes into `main`. It shows the diff and gives people a place to review and comment *before* the code is accepted. **This is where code review happens.**

**Merge**: Accepting a PR's changes into the `main` branch. **Squash merge** = combine all the PR's commits into one tidy commit when merging.

**Review actions on a PR**: *Comment* (leave notes, no decision), *Approve* (looks good, can merge), *Request changes* (must fix before merging).

**Draft PR**: A pull request marked "work in progress" so reviewers know it is not ready yet.

---

## Automation: the tools that review code for you

**Automation**: Letting software, not a person, catch routine problems. The idea behind our Layer 1-3: machines check the boring, mechanical stuff so humans can focus on judgement.

**Linter / Linting**: A tool that automatically reads your code and flags likely mistakes and bad patterns - unused variables, undefined names, risky constructs - *without running the code*. Examples: `ruff`/`flake8` (Python), `eslint` (JavaScript). *Think of it as spell-check and grammar-check for code.*

**Formatter / Formatting**: A tool that automatically rewrites your code into a consistent style (spacing, line breaks, quotes) so nobody argues about layout. Examples: `black` (Python), `prettier` (JS). *Removes all style debates from review.*

**Type checker**: A tool that verifies you are using data of the right kind - e.g., not passing text where a number is expected - before the code runs. Example: `mypy` (Python). *Catches a whole class of bugs early.*

**Test / Unit test**: A small piece of code whose only job is to check that your real code does what it should. It gives your code an input and confirms the output is correct. *If tests pass, you have evidence the code works - not just that it compiles.*

**Test suite**: All the tests for a project, run together.

**Test coverage**: How much of your code is exercised by tests, as a percentage. Higher is generally better (but 100% is not the goal).

**TDD (Test-Driven Development)**: Writing the test *first*, then the code to make it pass.

**Git hook**: A script that Git runs automatically at a certain moment - for example, right before you commit. *It lets you block a commit that fails checks.*

**pre-commit hook**: A hook that runs *before* a commit is saved. We use it to run the linter, formatter, and secret scanner on every commit automatically. If something fails, the commit is stopped until you fix it.

**pre-commit (the tool)**: A popular program (`pre-commit.com`) that manages these hooks for you via one config file, [`.pre-commit-config.yaml`](templates/.pre-commit-config.yaml). *This is your "always-on first reviewer," especially if you work solo.*

**CI (Continuous Integration)**: A service that automatically runs your tests and checks on a server every time you push code or open a PR. It reports pass/fail on the PR. *It is a tireless reviewer that never forgets to run the tests.*

**GitHub Actions**: GitHub's built-in CI. You describe the checks in a small file and GitHub runs them for you.

**CI pipeline**: The ordered sequence of automated steps CI runs (e.g., install → lint → test → security scan).

**CD (Continuous Delivery / Deployment)**: the step that comes after CI. Once the checks pass, CD automatically packages and ships the code to a staging or production environment. Review and CI decide whether a change is *good*; CD is about getting an approved change *out*. Code review mostly concerns CI, not CD.

---

## Security terms

**Secret**: Any sensitive credential that must stay private: passwords, API keys, database connection strings, access tokens, private keys. *Leaking one can let an attacker into your systems.*

**Secret scanning**: A tool that searches your code (and its history) for accidentally committed secrets and blocks or flags them. Examples: `gitleaks`, `TruffleHog`, GitHub's built-in secret scanning. *Because once a secret is pushed to GitHub, assume it is compromised.*

**SAST (Static Application Security Testing)**: A security tool that scans your source code for known vulnerability patterns - like SQL injection or unsafe input handling - *without running it*. Examples: CodeQL, Semgrep, Bandit (Python). *"Static" = it reads the code; it does not execute it.*

**DAST (Dynamic Application Security Testing)**: The opposite of SAST: it tests a *running* application by attacking it like a hacker would. (Less common in day-to-day review.)

**Dependency**: Outside code your project relies on (libraries/packages you install). A typical project has hundreds.

**Dependency scanning / SCA (Software Composition Analysis)**: Checking your dependencies for known security vulnerabilities. *You can write perfect code and still be hacked through a vulnerable library.*

**Supply chain (software)**: All the external code, tools, and services that go into building your software. A "supply-chain attack" compromises you through one of those, not your own code directly.

**Injection**: A class of attack where an attacker sneaks malicious input that your code mistakenly treats as commands (e.g., SQL injection into a database query). *A top cause of breaches; reviewers check that all external input is validated.*

**Encryption at rest / in transit**: *At rest* = data is scrambled while stored on disk. *In transit* = data is scrambled while traveling over the network (via **TLS**, the "s" in https). Both required for patient data.

**TLS**: The encryption that protects data moving over the internet. "TLS 1.2+" means use a modern, secure version.

**KMS (Key Management Service)**: An AWS service that manages the encryption keys used to scramble your data at rest.

**IAM (Identity and Access Management)**: The AWS system that controls *who* and *what* can access *which* resources.

**Least privilege**: Give each person/program the *minimum* access they need to do their job, and nothing more. *So a compromised component cannot reach everything.*

**Audit log**: An automatic, tamper-resistant record of who did what and when. On AWS this is **CloudTrail**. *Required for compliance and for investigating incidents.*

---

## The adversarial (red/blue team) terms

**Adversarial review**: A review done while deliberately *thinking like an attacker* instead of a builder. Instead of "does this work?" you ask "**how could someone abuse this?**"

**Attacker hat ("putting on the attacker hat")**: A figure of speech for switching your mindset to that of a malicious hacker for a few minutes, to spot weaknesses a builder would not notice.

**Threat**: Anything that could go wrong on purpose: someone stealing data, tampering with records, crashing the service, etc.

**Threat modeling**: A structured way to list the threats to a system *before* they happen, by looking at it from an attacker's point of view, then deciding how to defend against each.

**STRIDE**: A widely adopted threat-modeling checklist — created by Microsoft and referenced by NIST and OWASP — that breaks threats into six categories so non-experts can threat-model systematically. It is a solid foundation for general software security but does not cover ML/AI-specific threats (model poisoning, membership inference, adversarial inputs); for projects with ML components, pair it with the [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/). The letters stand for:
- **S**poofing - pretending to be someone/something else.
- **T**ampering - changing data you should not.
- **R**epudiation - doing something and denying it, because nothing was logged.
- **I**nformation disclosure - leaking data that should be private (e.g., PHI).
- **D**enial of service - overwhelming or breaking the system so others cannot use it.
- **E**levation of privilege - gaining more access than you are supposed to have.

**STRIDE-lite**: Our lightweight version: six yes/no questions on the PR (one per STRIDE letter) so even a beginner can do a basic security pass.

**Red team**: People who play the attacker and try to break into a system (offense).

**Blue team**: People who defend the system and try to detect/stop attacks (defense).

**Purple team**: Red and blue working together in a loop: attackers find a hole, defenders fix it and add detection. *Our "adversarial pass + detection follow-up" is a miniature purple team.*

**Security champion**: One team member designated to carry the security perspective into everyday work and reviews. *A lightweight alternative to a full security team - ideal for a small group.*

---

## Health-data terms

**PHI (Protected Health Information)**: Any health data that can be tied to a specific person (name, medical record number, diagnosis, etc.). Legally protected. *Leaking PHI is a reportable breach with real consequences.*

**HIPAA**: The US law that governs how PHI must be protected. Its "Security Rule" lists safeguards that software must meet.

**De-identification**: Removing or masking the details that could identify a patient, so data can be used for analysis without exposing people.

**EHR (Electronic Health Record)**: The digital patient record system in a hospital (e.g., EPIC).

**FHIR ("fire", Fast Healthcare Interoperability Resources)**: The standard data format for health information, so different systems can exchange it. Everything is a structured "resource" (Patient, Encounter, Observation, ...).

**Synthetic data (e.g., Synthea)**: Fake, computer-generated patient data that looks realistic but corresponds to no real person. *Use it in tests and demos - never real PHI.*

---

## Machine-learning / reproducibility terms

**Model**: The trained output of a machine-learning process that makes predictions.

**Train/test split; train-test leakage**: You train a model on one chunk of data and test it on a separate chunk. **Leakage** = test information accidentally bleeds into training, making the model look better than it really is. *A reviewer checks splits are clean and done at the patient level.*

**Seed**: A fixed starting number that makes a "random" process repeatable, so you get the same result every run. *Essential for reproducibility.*

**Reproducibility**: The ability to run the same code + data later and get the same result. *A core requirement for research and audits.*

**Data/model versioning**: Tracking versions of datasets and trained models, not just code. Tool: **DVC (Data Version Control)**, which works alongside Git.

**Model card**: A short standard document describing a model: what it does, how well it performs (broken down by group), and its limits.

**Datasheet (for a dataset)**: A standard document describing a dataset's origin, contents, and appropriate uses.

**Drift**: When real-world data gradually changes so a model's accuracy degrades over time. *Needs monitoring after deployment.*

---

## Review culture & process terms

**Code review**: One or more people (or tools) examining a change before it is merged, to catch bugs, improve quality, and share knowledge.

**Author**: The person who wrote (or prompted an AI to write) the change.

**Reviewer**: The person examining the change.

**Code health**: The overall long-term quality and maintainability of the codebase. Our approval bar: *approve when the change improves code health* - it does not have to be perfect.

**Bus factor**: How many people would have to "get hit by a bus" before a project is in trouble because only they understood the code. *Review raises the bus factor by spreading knowledge.* A bus factor of 1 (solo, no review) is risky.

**Technical debt**: Shortcuts in code that save time now but cost more later. Review helps keep it in check.

**Blast radius**: how much could break if a change is wrong. Used to decide how deep a review must be: a small blast radius allows a lighter review, a large one requires a full line-by-line review.

**Vanity metric**: a number that is easy to measure and looks like quality but does not guarantee it, such as code-coverage percentage or linter-violation counts.

**Nit (nitpick)**: A minor, optional comment (usually style/preference). We prefix these `nit:` so the author knows they are not blocking.

**Conventional Comments**: A simple standard for labeling review comments by intent - `praise:`, `nitpick:`, `suggestion:`, `issue:`, `question:`, `thought:`, `chore:`, plus `(blocking)`/`(non-blocking)`. Makes feedback clear and kind. See [conventionalcomments.org](https://conventionalcomments.org/).

**Blocking vs non-blocking**: *Blocking* = must be resolved before merge. *Non-blocking* = optional / author's call.

**CODEOWNERS**: A file that says who must approve changes to which parts of the code. GitHub auto-requests their review.

**Branch protection**: GitHub settings that enforce rules on `main` - e.g., "requires one approval and passing CI before merge."

**SLA (Service Level Agreement)**: Here, an agreed response time - e.g., "reviewers respond within one business day."

**Readability (Google's model)**: A certification that a person knows a language's standards well enough that their approval covers style/idioms. (A large-team concept; mentioned for completeness.)

---

## AI-coding terms

**AI coding assistant**: A tool that writes or suggests code from your instructions. Examples: GitHub Copilot, Claude Code, Cursor, Gemini.

**LLM (Large Language Model)**: The kind of AI behind these assistants (and ChatGPT). It predicts likely text/code; it does not truly "understand" or run the code.

**Prompt**: The instruction you give the AI.

**Context**: The information you give the AI to work with (relevant files, docs, constraints). More/better context = fewer mistakes.

**Hallucination**: When an AI confidently produces something false - e.g., calling a function or library that does not actually exist. *A key thing to check when reviewing AI code.*

**Agent**: An AI that can take multiple steps on its own (read files, run tests, edit code) rather than just answering once.

**Rules file (`CLAUDE.md`, `GEMINI.md`, Copilot/Cursor instructions)**: A file where you write standing instructions for the AI (your style, do's and don'ts) so it follows your conventions automatically.

**Spec (`spec.md`)**: A short written description of what you are building and its requirements, written *before* coding. *Especially important with AI - plan first, generate second.*

**Automation bias**: The human tendency to over-trust automated/AI output and under-check it. *A documented, dangerous trap - name it and fight it.*

**The "70% problem"**: Addy Osmani's observation that AI gets you ~70% of the way fast, but the last 30% (correctness, edge cases, polish) still needs real engineering judgement - which is exactly where review matters.

**Context rot**: the gradual drop in an AI model's output quality as its context window fills up. A practical rule is to keep a task to about 40% of the window.

**Coherence problem**: AI-generated code that is correct locally but does not fit together globally: overlapping solutions, abstractions that do not compose, and drifting names. Because each piece looks clean, the drift is easy to miss.
