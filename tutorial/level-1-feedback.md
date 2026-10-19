# Level 1 - Giving & Receiving Feedback

**Goal:** write review comments that are clear, kind, and useful - and receive them without taking it personally. This is the hardest *soft* skill in review, and the one beginners get wrong most.

> Prerequisite: [Level 0](level-0-mechanics.md). New words are in the [Glossary](../GLOSSARY.md).
> Practice it: [exercises/level-1-feedback](../exercises/level-1-feedback/).

---

## 1. The problem with ordinary comments

Most review comments are unclear about **how serious they are**. Is "this function is long" a demand, or a passing thought? The author cannot tell, so they either over-react to trivia or ignore something important. The fix is a tiny shared vocabulary.

---

## 2. Conventional Comments (our standard)

Start every comment with a **label** that says what kind of comment it is, and optionally whether it **blocks** merging. Standard: [conventionalcomments.org](https://conventionalcomments.org/).

```
<label> [(blocking|non-blocking)]: <your message>
```

Labels we use:
| Label | Means | Example |
|---|---|---|
| `praise:` | Something genuinely good (say these out loud!) | `praise: nice clear error message here.` |
| `nitpick:` | Minor, optional, usually style | `nitpick (non-blocking): rename tmp → parsed_date?` |
| `suggestion:` | A concrete proposed change | `suggestion: extract this into a helper so it is testable.` |
| `issue:` | A real problem that should be fixed | `issue (blocking): this crashes when value is empty.` |
| `question:` | You want to understand before judging | `question: is this path reachable if auth fails?` |
| `thought:` | A non-blocking idea for later | `thought: we could cache this someday.` |
| `chore:` | A small required task | `chore: add this file to .gitignore.` |

**`(blocking)`** = must be resolved before merge. **`(non-blocking)`** = author's call.

**The `nit:` convention:** many teams (including Google) prefix trivial comments with `nit:` so the author instantly knows it is optional. Conventional Comments' `nitpick:` is the same idea, formalized.

---

## 3. How to give good feedback

Grounded in Google's "[How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html)":

- **Comment on the code, not the person.** "This function does X" not "You always do X."
- **Explain *why*.** "`issue: this re-reads the file on every call, which is slow - can we read it once?`" teaches; "`this is wrong`" does not.
- **Ask, do not command.** Questions invite discussion and are often how *you* learn the author had a good reason.
- **Be specific and actionable.** Point to the line; propose a direction.
- **Balance it.** A `praise:` costs nothing and makes the rest land better.
- **Do not pile on nits.** If the big picture needs rework, hold the trivia for later.

### Before / after
- ❌ "This is messy and wrong."
- ✅ `issue (blocking): parse_dob crashes on an empty string (see test case). Can we return None and let the caller handle it?`

---

## 4. How to receive feedback (the half everyone skips)

Grounded in Google's "[How to handle reviewer comments](https://google.github.io/eng-practices/review/developer/handling-comments.html)":

- **Do not take it personally.** The review is about the code, not you. This is genuinely hard at first and gets easier fast.
- **Assume good intent.** The reviewer is trying to help the project.
- **Fix the code, do not argue in the thread.** If a reviewer misread something, that itself is a signal the code could be clearer.
- **Disagree productively.** It is fine to push back *with reasoning*. If you are stuck, escalate to a third person rather than warring in comments.
- **Resolve, do not ignore.** Reply to or address every `(blocking)` comment.

---

## 5. Hands-on (~45 min)

1. Read the three short Google pages: [comments](https://google.github.io/eng-practices/review/reviewer/comments.html), [handling comments](https://google.github.io/eng-practices/review/developer/handling-comments.html), and the [Conventional Comments](https://conventionalcomments.org/) home page.
2. **Rewrite exercise:** take these blunt comments and rewrite them as Conventional Comments:
   - "why is this here"
   - "wrong"
   - "too long"
   - "I would do this differently"
3. **Real practice:** review a teammate's (or a sample) PR and leave at least one `praise:`, one `suggestion:`, and one `question:`.

### Level 1 deliverable
- [ ] Reviewed a PR using labeled Conventional Comments, including at least one piece of praise.
- [ ] Received feedback on one of your own PRs and resolved it gracefully.

---

## Solo note
You are both author and reviewer, so practice the *giving* voice on your own diff: write labeled comments to yourself on your PR (`question: is this edge case handled?`). It forces the reviewer mindset and the notes are useful when you come back later.

---

**Next:** [Level 2 - Systematic review & automation →](level-2-systematic.md)
