# MIT License
#
# Copyright (c) 2021 ESCAPE
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from pyspark.sql import SparkSession

import sys
import json


def main():
    spark = SparkSession.Builder().getOrCreate()

    # Set spark log level to WARN
    spark.sparkContext.setLogLevel("WARN")

    msg = """
    \nSpark configuration\n-------------------
    """
    print(msg)
    print(spark.version)
    print(spark.sparkContext.getConf().getAll())

    print('Reading some data...')
    df = spark.read.format('parquet').load('data/clusters.parquet')
    df.count()
    print('Configuration OK!')

    msg = """
    \nPython configuration\n--------------------
    """
    print(msg)
    print(sys.version)

    msg = """
    \nJupyter RISE add-ons\n--------------------
    """
    print(msg)
    with open('../.jupyter/nbconfig/rise.json') as f:
        rise_info = json.load(f)
    print(rise_info)


if __name__ == '__main__':
    main()
