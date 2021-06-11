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
import pandas as pd

import os

from tester import spark_unit_tests


def compute_barycentre(pdf: pd.DataFrame) -> pd.DataFrame:
    """ Compute the barycentre of a partition

    Parameters
    ----------
    pdf : pandas DataFrame
        pandas DataFrame containing partition data

    Returns
    ----------
    Pandas DataFrame with barycentre coordinates.

    Examples
    ----------
    >>> df = spark.read.format('parquet').load(datapath)

    >>> df_grouped = df.groupBy("id")\
        .applyInPandas(compute_barycentre, schema=df.schema)

    # Check you have 3 clusters
    >>> df_grouped.count()
    3
    """
    mean = pdf.mean()

    out = {colname: [value] for colname, value in zip(mean.keys(), mean.values)}

    return pd.DataFrame(out)


if __name__ == "__main__":
    """ Execute the test suite """

    globs = globals()
    path = os.path.dirname(__file__)

    globs["datapath"] = 'file://{}/../data/clusters.parquet'.format(path)

    # Run the test suite
    spark_unit_tests(globs)
