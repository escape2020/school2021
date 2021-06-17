#!/bin/bash
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
docker build -t "spark_escape2021" -f Dockerfile .

SPARKFITS="com.github.astrolabsoftware:spark-fits_2.12:0.9.0"

# Check installation worked
docker run -it --rm  \
  -v $PWD:/home/jovyan/work:rw -p 8888:8888 -p 4040:4040 -p 18080:18080 \
  spark_escape2021 spark-submit --master local[*] \
  --driver-memory 2g --executor-memory 2g --packages $SPARKFITS test_installation.py

# Run unit tests
docker run -it --rm  \
  -v $PWD:/home/jovyan/work:rw -p 8888:8888 -p 4040:4040 -p 18080:18080 \
  spark_escape2021 ./test.sh
