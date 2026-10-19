# Exercise: A full priority-order review

Practices [Level 2](../../tutorial/level-2-systematic.md). Time: about 40 minutes.

The folder [`sample-project/`](sample-project/) contains a tiny Python module, `stats.py`, and its tests, `test_stats.py`. The tests pass, so continuous integration would show a green check. Your job is to review the change the way a human should: find what the tests miss.

## Steps

1. **Run the automation (Layers 1 and 3).** From inside `sample-project/`:
   ```bash
   pip install pytest
   pytest
   ```
   The tests pass. Optionally, copy the repo's [`.pre-commit-config.yaml`](../../templates/.pre-commit-config.yaml) and [`github-actions-ci.yml`](../../templates/github-actions-ci.yml) in and run them, to see the automated layers in action.

2. **Do the human review (Layer 4), in priority order.** Use the [review checklist](../../templates/review-checklist.md). Go in this order and write down what you find:
   - Correctness: what inputs make each function behave badly or crash?
   - Tests: which cases are not covered?
   - Readability: anything unclear?
   - Style: leave this to the formatter.

3. **Write your findings as [Conventional Comments](https://conventionalcomments.org/)** (`issue:`, `suggestion:`, and so on, with `(blocking)` where needed).

4. **Add the missing tests** for the edge cases you found, then propose a fix for each bug.

Hint: there are three correctness problems, one in each function. All three involve an input the happy-path tests never try.

When you are done, open [answer-key.md](answer-key.md).
