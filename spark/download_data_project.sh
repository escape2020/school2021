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

# Catalog data (~140MB compressed, 160MB uncompressed)
curl https://owncloud.lal.in2p3.fr/index.php/s/PLTp7BRirtVOX1s/download -o data/catalogs.zip
unzip data/catalogs.zip -d data
rm data/catalogs.zip

# image data (~50MB compressed, 150MB uncompressed)
curl https://owncloud.lal.in2p3.fr/index.php/s/xMz0n5EIMT67XXx/download -o data/images.zip
unzip data/images.zip -d data
rm data/images.zip
