from astropy.table import Table
import numpy as np


def test_to_csv(tmp_path):

    t = Table({'a': [1, 2, 3], 'b': [4, 5, 6]})
    t.write(tmp_path / 'test.csv')

    read = Table.read(tmp_path / 'test.csv')
    assert np.all(read == t)
