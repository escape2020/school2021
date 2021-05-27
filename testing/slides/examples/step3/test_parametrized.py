import pytest

n = range(9)
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21]

@pytest.mark.parametrize('n,expected', zip(n, fibs))
def test_fibonacci(n, expected):
    from fibonacci import fibonacci

    assert fibonacci(n) == expected
