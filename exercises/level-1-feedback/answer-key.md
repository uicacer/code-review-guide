# Answer key: Rewrite review comments

These are model rewrites. Yours do not need to match word for word. What matters is the right label, a correct blocking/non-blocking call, a focus on the code, and a clear *why*.

First, note the real defect in the sample code: when no user matches `user_id`, the function returns `users[0]` instead of signalling "not found." That is a genuine bug, so the comment about it should block.

1. "this is wrong"
   `issue (blocking): when no user matches user_id, this returns users[0] instead of None. A caller asking for a missing user would silently get the wrong user. Can we return None (or raise) instead?`

2. "why return users[0]??"
   `question (blocking): what is the intent of returning users[0] on no match? If it is a fallback it looks unsafe; if it is a mistake we should return None. Blocking until we confirm.`
   (A `question` can block when the answer decides correctness.)

3. "no tests"
   `issue (blocking): there are no tests for this function. Please add at least a match case and a no-match case, since the no-match path is where the bug hides.`

4. "variable name u is bad"
   `nitpick (non-blocking): consider renaming u to user for readability.`

5. "this loop is slow"
   `thought (non-blocking): for large user lists a linear scan on every call could add up. Not a problem now; noting it in case this gets hot.`

6. "I would use a dict"
   `suggestion (non-blocking): if lookups happen often, building a {id: user} dict once would make this O(1). Optional for this PR.`

7. "nice"
   `praise: clean early-return structure, easy to follow.`

8. "add a docstring"
   `chore (non-blocking): add a one-line docstring describing the return value, especially the no-match behaviour once we decide it.`

## Part 2: receiving feedback

A healthy response to a sharp `issue (blocking)`:

> "Good catch, the users[0] fallback was a mistake. I will change it to return None and add a no-match test." Then fix the code and reply on the thread confirming it is done.

The point: do not take the tone personally, fix the code rather than argue, and close the loop so the reviewer knows it was handled. If you disagreed, you would explain your reasoning calmly and, if still stuck, ask a third person rather than going back and forth.
