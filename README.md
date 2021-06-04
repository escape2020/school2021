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

[Go to anaconda](https://www.anaconda.com/products/individual) and follow install instructions for your OS.

If you had already installed anaconda in the past, you might want to update it:
```
conda update -n base --all
```

### clone the repository

Open a terminal and go to your working directory

```
git clone --recursive https://github.com/escape2020/school2021.git
```

The `--recursive` is needed because we use submodules for the LaTeX slides and
the web page. You can leave it out in case you don't want to build the slides or web page.

If you cloned without recursive and need the submodules, run
```
cd school2021
git submodule update --init --recursive
```

### Setup the conda environment

We recommend the use of [mamba](https://github.com/mamba-org/mamba) to solve environment dependencies.    
However, you may use only conda (just replace `mamba` commands with `conda`).

```
cd school2021
conda install mamba -n base -c conda-forge
mamba env create -f environment.yml
conda activate eschool2021
```

If you have already created the `eschool2021` env previously, you can update it using:

```
conda activate eschool2021
mamba env update -f environment.yml
```




# binder

You may run the content of this repository on [mybinder service](https://mybinder.readthedocs.io/en/latest/).
This should be used rather for test purposes, if you are participating to the school, you should install the virtual environment as explained above and run courses and exercises for yourself.

[![badge](https://img.shields.io/badge/run-mybinder-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/escape2020/school2021/7081ab31079e04fdfa5b8e4fe6678614af5a5583)

---

# Install Docker
Some lectures will require the usage of [containers](https://www.docker.com/resources/what-container) to exemplify big data processing and software reproducibility.

*Do not worry, like with Git, you will get an introduction and hands-on sessions on containers during the school.*

[Docker documentation](https://docs.docker.com/engine/install/) is great. So, please use this **[link](https://docs.docker.com/engine/install/)**, find the Docker Desktop app that matches your Operative System, download and installs it.

**Important** For Windows users, it is possible that you will need to enable the virtualization in your machine (it comes disabled by default by some vendors). However, this is **highly** vendor/hardware-dependent, making it impractical to list a series of instructions.

For that reason, the best option is to Google ```enable virtualization in windows X``` where ```X``` is your Windows OS version. And/or search for ```enable virtualization in YZ``` where ```YZ``` is your machine brand/model.
