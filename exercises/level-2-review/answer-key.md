# Answer key: A full priority-order review

## The three correctness problems (all on untested paths)

1. **`mean([])` crashes** with `ZeroDivisionError`, because `len(values)` is 0. An empty list is a normal input a caller might pass.
2. **`percent_change(0, x)` crashes** with `ZeroDivisionError`, because `old` is in the denominator. A starting value of 0 is realistic.
3. **`last_n(values, 0)` returns the whole list**, not an empty list. `values[-0:]` is the same as `values[0:]`, which is every element. This is the subtle one, and it is wrong: asking for the last zero items should give nothing.

The happy-path tests never try an empty list, a zero starting value, or `n = 0`, which is why CI is green while the code is buggy. This is the core lesson: **green automation means the checks you wrote passed, not that the code is correct.**

## Example review comments

- `issue (blocking): mean([]) raises ZeroDivisionError. Empty input is plausible. Can we raise a clear ValueError, or define a documented return for the empty case?`
- `issue (blocking): percent_change divides by old, so old=0 crashes. Please guard against a zero starting value.`
- `issue (blocking): last_n(values, 0) returns the full list because values[-0:] equals values[:]. It should return []. Please handle n <= 0.`
- `issue (blocking): no tests cover empty input, old=0, or n=0, which is exactly where the bugs are. Please add them.`

## The missing tests

```python
import pytest
from stats import mean, percent_change, last_n


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_percent_change_zero_old():
    with pytest.raises(ValueError):
        percent_change(0, 10)


def test_last_n_zero():
    assert last_n([1, 2, 3], 0) == []
```

## A reasonable fix

```python
def mean(values):
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def percent_change(old, new):
    """Return the percentage change from old to new."""
    if old == 0:
        raise ValueError("percent_change() requires a non-zero old value")
    return (new - old) / old * 100


def last_n(values, n):
    """Return the last n items of values."""
    if n <= 0:
        return []
    return values[-n:]
```

## What you practiced
- Reviewing in priority order, correctness before style.
- Seeing that passing tests and green CI do not prove correctness.
- Turning findings into clear, labeled comments.
- Closing the loop by adding the tests that should have existed.
