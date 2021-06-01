from astropy.table import Table
import numpy as np
import pytest

@pytest.fixture(scope='session')
def my_tmp_path(tmp_path_factory):
    return tmp_path_factory.mktemp('foo')


def test_to_csv(my_tmp_path):

    t = Table({'a': [1, 2, 3], 'b': [4, 5, 6]})
    t.write(my_tmp_path / 'test.csv')

    read = Table.read(my_tmp_path / 'test.csv')
    assert np.all(read == t)
