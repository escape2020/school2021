import pytest

@pytest.mark.xfail
def test_this_fails():
    import math
    assert math.pi == 3
