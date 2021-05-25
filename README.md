# ESCAPE data science summer school 2021

All information on the school may be found on the main page:     
https://indico.in2p3.fr/event/20306/

## School Program:

The school is devoted to project development for astrophysics, astroparticle physics & particle physics.    
The aim of the school is to provide theoretical and hands-on training on Data Science and Python development (coding environment and good code practices, version control and collaborative development, Python packaging, scientific libraries for data science and analysis and machine learning).

The lectures content may be found here:
https://escape2020.github.io/school2021/

## Setup

![env workflow](https://github.com/escape2020/school2021/actions/workflows/python-package-conda.yml/badge.svg)


### Install anaconda

[Go to anaconda](https://www.anaconda.com/products/individual) and install it.


### clone the repository

Open a terminal and go to your working directory

```
git clone https://github.com/escape2020/school2021.git
```

### Setup the conda environment

```
cd school2021
conda env create -f environment.yml
conda activate eschool2021
```

If you have already created the `eschool2021` env previously, you can update it using:

```
conda activate eschool2021
conda env update -f environment.yml
```

