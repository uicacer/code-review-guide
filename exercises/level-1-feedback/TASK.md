# Exercise: Rewrite review comments

Practices [Level 1](../../tutorial/level-1-feedback.md). Time: about 20 minutes.

Below are eight real-sounding but poor review comments. Each is vague, blunt, or unclear about whether it blocks the merge. Your job is to rewrite each one as a [Conventional Comment](https://conventionalcomments.org/):

```
<label> [(blocking|non-blocking)]: <clear, specific, kind message that explains why>
```

Labels: `praise`, `nitpick`, `suggestion`, `issue`, `question`, `thought`, `chore`.

Rules you are practicing:
- Pick the right label.
- Mark `(blocking)` only when it must be fixed before merge.
- Comment on the code, not the person.
- Explain *why*, and make it actionable.

## The comments to rewrite

The code under review is a small Python function:

```python
def get_user(users, user_id):
    for u in users:
        if u.id == user_id:
            return u
    return users[0]
```

1. "this is wrong"
2. "why return users[0]??"
3. "no tests"
4. "variable name u is bad"
5. "this loop is slow"
6. "I would use a dict"
7. "nice"
8. "add a docstring"

## Part 2: receiving feedback

Imagine you are the author and you receive comment 2 as a sharp `issue (blocking)`. Write two sentences describing how you would respond in a healthy way (what you do in the code and in the thread). Then compare with the answer key.

When you are done, open [answer-key.md](answer-key.md).
