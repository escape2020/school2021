import numpy as np

def test_sin():
    x = np.array([0, np.pi / 2, np.pi])
    np.testing.assert_array_almost_equal(np.sin(x), [0, 1, 0], decimal=15)

def test_poly():
    def f(x):
        return x**2 + 2 * x + 10

    x = np.array([0.0, 1.0, 2.0])
    np.testing.assert_allclose(f(x), [10.0, 13.0, 18.0], rtol=1e-5)
