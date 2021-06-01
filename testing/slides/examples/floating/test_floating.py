import pytest

def test_addition_naive():
    assert 0.1 + 0.2 == 0.3

def test_addition_correct():
    assert 0.1 + 0.2 == pytest.approx(0.3)
