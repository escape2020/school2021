import pytest
import sys
import os

def test_using_numpy():
    np = pytest.importorskip("numpy")
    assert len(np.zeros(5)) == 5

@pytest.mark.skipif(sys.platform != 'win32', reason="windows only")
def test_windows():
    assert os.path.exists('C:\\')
