# README

Supplementary example in a python script for machine learning section.

These examples use a number of other libraries for doing embedding which are not in the base environment
that you will need to install:
- [pacmap](https://pypi.org/project/pacmap/) `pip install pacmap`
- [umap](https://pypi.org/project/umap-learn/) `pip install umap-learn`
- [pymde](https://pymde.org/) `pip install pymde`
- [trimap](https://pypi.org/project/trimap/) `pip install trimap`

The libraries are still being tested, and their interfaces may change, but they build on
 [t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding).

The example uses a portion of the 200Mb
[Galaxy10SDSS dataset](https://astronn.readthedocs.io/en/latest/galaxy10sdss.html)
which can be downloaded from http://astro.utoronto.ca/~bovy/Galaxy10/Galaxy10.h5 . 

Another classification example is available in the
[AstroNN documentation](https://astronn.readthedocs.io/en/latest/galaxy10sdss.html). 
