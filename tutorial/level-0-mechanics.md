# Level 0 - Mechanics & Vocabulary

**Goal:** remove all the confusing machinery so that, by the end, you have opened a pull request and reviewed one - and you know what every word means.

No prior experience needed. If a term is new, it is in the [Glossary](../GLOSSARY.md).

---

## 1. Why code review exists (30-second version)

Before code becomes part of a shared project, someone (or something) checks it. That check:
- catches bugs before users hit them,
- spreads knowledge so a project does not depend on one person (raises the [bus factor](../GLOSSARY.md#review-culture--process-terms)),
- keeps the codebase understandable over time.

In the AI era this matters *more*, not less: AI writes code fast and confidently, including confident mistakes. Review is how we stay accountable for what ships.

---

## 2. The vocabulary, built up in order

Read these in sequence - each builds on the last. (All also in the [Glossary](../GLOSSARY.md).)

1. **[Version control](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: software that records every change to your code, like "track changes" for a whole project. The tool is **Git**.
2. **[Repository ("repo")](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: your project folder, tracked by Git, with its full history.
3. **[GitHub](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: a website that stores repos online so people can share and review.
4. **[Commit](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: one saved snapshot of changes, with a message. A "save point."
5. **[Branch](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: a parallel workspace so you can make changes without disturbing the main code. The main one is `main`.
6. **[Push / Pull](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: upload / download commits between your laptop and GitHub.
7. **[Diff](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: the exact lines added (`+`) and removed (`-`). **Reviewing code = reading a diff.**
8. **[Pull Request ("PR")](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: a request to merge your branch into `main`. It shows the diff and is where review happens.
9. **[Merge](../GLOSSARY.md#the-basics-git-branches-and-pull-requests)**: accepting the PR's changes into `main`.

### The normal flow (the "GitHub flow")
```
make a branch → commit your work → push → open a Pull Request →
   people review → you address comments → approve → merge → delete the branch
```
That loop is the backbone of everything else.

---

## 3. What a reviewer actually sees

Open any PR on GitHub and click the **"Files changed"** tab. You will see the **diff**:

```diff
  def parse_dob(value):
-     return datetime.strptime(value, "%m/%d/%y")
+     return datetime.strptime(value, "%m/%d/%Y")   # 4-digit year
```
- Red `-` line = removed. Green `+` line = added.
- You can click any line to leave a **comment**.
- When done, you submit a review as one of three actions:
  - **Comment**: notes, no decision.
  - **Approve**: looks good to merge.
  - **Request changes**: must be fixed before merging.

A PR marked **Draft** means "work in progress - do not review yet."

---

## 4. Hands-on (do this for real - ~60-90 min)

The fastest way to learn the mechanics is GitHub's own free interactive courses. They run inside a real repo and walk you through each click.

1. **Introduction to GitHub**: https://github.com/skills/introduction-to-github
   *You will create a branch, make a commit, and open your first pull request.*
2. **Reviewing pull requests**: https://github.com/skills/review-pull-requests
   *You will request a review, leave comments, and suggest changes.*

Then, to connect it to day-to-day work, read GitHub's short explainer:
- **GitHub flow**: https://docs.github.com/en/get-started/using-github/github-flow
- **About pull request reviews**: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews

### Level 0 deliverable
On a throwaway or practice repo:
- [ ] Create a branch, make a small change, commit it with a clear message, push it.
- [ ] Open a pull request with a one-paragraph description.
- [ ] On a peer's PR (or the course's sample PR), leave one comment and submit a review.

If you did those three things, you have used every core mechanic. 🎉

---

## Solo note
Even alone, **use branches and PRs on yourself.** Opening a PR - even one only you will read - gives you a clean place to see your own diff and review it before merging. Think of the PR description as "a message to your future self."

---

**Next:** [Level 1 - Giving & receiving feedback →](level-1-feedback.md)
