# Tutorials for the Introduction to Deep Learning course of 2021 ESCAPE Summer School

First, create the conda environment on your machine:
```
conda create -n dl_escape python=3.8
```
Then, install PyTorch (pytorch.org), jupyter and other dependencies
```
conda activate dl_escape
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
conda install jupyter
conda install matplotlib
pip install tensorboard
pip install pytorch-lightning
```

Then, run all cells of T0_hands_on_preparation.ipynb

You also need to download the data for tutorial 5: https://zenodo.org/record/5226945/files/cats_dogs_light.zip?download=1
and unzip the file in './data' 

# Tutorial list: 
### Deep learning basics
1\. Fitting a noisy sin with a MLP

2\. A binary classification with a MLP

3\. A multi-class classification with a MLP
### Let's dive deep !
4\. Introduction to Lightning with CIFAR10 classification

5\. Transfer learning on Cats and Dogs


