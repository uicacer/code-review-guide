"""Small statistics helpers. Sample code for the Level 2 review exercise.

This code is deliberately imperfect. Your job in the exercise is to review it.
"""


def mean(values):
    """Return the arithmetic mean of a list of numbers."""
    return sum(values) / len(values)


def percent_change(old, new):
    """Return the percentage change from old to new."""
    return (new - old) / old * 100


def last_n(values, n):
    """Return the last n items of values."""
    return values[-n:]
