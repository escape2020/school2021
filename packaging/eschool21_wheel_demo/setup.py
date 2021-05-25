from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("eschool21_wheel_demo/fibonacci.pyx")
)
