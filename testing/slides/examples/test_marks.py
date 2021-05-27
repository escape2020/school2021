import pytest
import time

@pytest.mark.slow
def test_slow():
    time.sleep(5)
    assert 1 + 1 == 2

def test_fast():
    assert 1 + 1== 2
