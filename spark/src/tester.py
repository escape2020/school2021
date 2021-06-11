from pyspark.sql import SparkSession
from pyspark import SparkConf

import sys
import doctest
import numpy as np


def spark_unit_tests(global_args: dict = None, verbose: bool = False):
    """ Base commands for the Spark unit test suite

    Include this routine in the main of a module, and execute:
    python3 mymodule.py
    to run the tests.

    It should exit gracefully if no error (exit code 0),
    otherwise it will print on the screen the failure.

    Parameters
    ----------
    global_args: dict, optional
        Dictionary containing user-defined variables to
        be passed to the test suite. Default is None.
    verbose: bool
        If True, print useful debug messages.
        Default is False.

    """
    if global_args is None:
        global_args = globals()

    conf = SparkConf()

    # Extra package for tests
    confdic = {
        "spark.python.daemon.module": "coverage_daemon"
    }

    # Use only 2 threads for tests
    conf.setMaster("local[2]")

    # Name of the test job
    conf.setAppName("test_spark_job")

    for k, v in confdic.items():
        conf.set(key=k, value=v)

    spark = SparkSession\
        .builder\
        .config(conf=conf)\
        .getOrCreate()

    global_args["spark"] = spark

    # Numpy introduced non-backward compatible change from v1.14.
    if np.__version__ >= "1.14.0":
        np.set_printoptions(legacy="1.13")

    sys.exit(doctest.testmod(globs=global_args, verbose=verbose)[0])
