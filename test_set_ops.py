from set_ops import intersection, union, difference, symmetric_difference
from random import sample

numbers = list(range(1000))


def random_set(size=500):
    return list(sample(numbers, size))


def intersection_alt(S1, S2):
    return sorted(set(S1) & set(S2))


def union_alt(S1, S2):
    return sorted(set(S1) | set(S2))


def difference_alt(S1, S2):
    return sorted(set(S1) - set(S2))


def symmetric_difference_alt(S1, S2):
    return sorted(set(S1) ^ set(S2))


def test_ops():
    for _ in range(100):
        S1, S2 = random_set(), random_set()
        assert intersection(S1, S2) == intersection_alt(S1, S2)
        assert union(S1, S2) == union_alt(S1, S2)
        assert difference(S1, S2) == difference_alt(S1, S2)
        assert symmetric_difference(S1, S2) == symmetric_difference_alt(S1, S2)
