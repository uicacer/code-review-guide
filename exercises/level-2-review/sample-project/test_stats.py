"""Tests for stats.py.

Notice: these tests only cover the easy "happy path." They pass, so CI would
show green. Part of the exercise is to see why green CI does not mean the code
is correct.
"""

from stats import mean, percent_change, last_n


def test_mean():
    assert mean([2, 4, 6]) == 4


def test_percent_change():
    assert percent_change(100, 150) == 50


def test_last_n():
    assert last_n([1, 2, 3, 4], 2) == [3, 4]
