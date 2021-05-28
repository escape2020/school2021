from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# this is a workaround for an issue in pip that prevents editable installs
# with --user, see https://github.com/pypa/pip/issues/7953
import site, sys; site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

fibonacci = Extension(
    "eschool21_cython_demo.fibonacci",
    ["eschool21_cython_demo/fibonacci.pyx"],
    include_dirs=[np.get_include()]
)

setup(
    ext_modules=cythonize([fibonacci]),
)
