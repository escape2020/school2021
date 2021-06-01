import pytest

@pytest.fixture(scope='session')
def some_data():
    return [1, 2, 3]

def test_using_fixture(some_data):
    assert len(some_data) == 3

def test_also_using_fixture(some_data):
    assert some_data[0] == 1
