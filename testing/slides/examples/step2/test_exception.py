import pytest

def test_invalid_values():
    from fibonacci import fibonacci

    with pytest.raises(ValueError):
        fibonacci(-1)
