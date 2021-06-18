# import everything we need first
import numpy as np
import h5py
import matplotlib.pyplot as plt
import pymde
import pacmap
import umap
import pymde
import trimap
from sklearn import decomposition
from sklearn import manifold
from sklearn.model_selection import train_test_split
import math

# To get the images and labels from file
with h5py.File('Galaxy10.h5', 'r') as F:
    images = np.array(F['images'])
    labels = np.array(F['ans'])

X_train = np.empty([math.floor(len(labels)/100),14283],dtype=np.float64)
y_train = np.empty([math.floor(len(labels)/100)],dtype=np.float64)
X_test = X_train
y_test = y_train

X_train = np.empty([math.floor(len(labels)/100),14283],dtype=np.float64)
y_train = np.empty([math.floor(len(labels)/100)],dtype=np.float64)
X_test = X_train
y_test = y_train
# Try to improve this by creating more balanced data subsets
# and using randomization
for i in range(math.floor(len(labels)/100)):
    X_train[i,:]=np.array(np.ndarray.flatten(images[i,:,:,:]),dtype=np.float64)
    y_train[i]=labels[i]
    X_test[i,:]=np.array(np.ndarray.flatten(images[i+math.floor(len(labels)/100),:,:,:]),dtype=np.float64)
    y_test[i]=labels[i+math.floor(len(labels)/100)]

# Plot distribution
classes, frequency = np.unique(y_train,return_counts=True)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.bar(classes,frequency)
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.title('Data Subset')
plt.savefig("galaxy10_subset.svg")

## 2D Embedding
### PCA
pca = decomposition.PCA(n_components=2)
pca.fit(X_train)
galaxy10_pca = pca.transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_pca[:, 0], galaxy10_pca[:, 1], c=y_train, cmap=plt.cm.nipy_spectral,
        edgecolor='k',label=y_train)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_pca.svg")

### trimap
galaxy10_trimap = trimap.TRIMAP().fit_transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_trimap[:, 0], galaxy10_trimap[:, 1], c=y_train, cmap=plt.cm.nipy_spectral,
        edgecolor='k',label=y_train)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_trimap.svg")

### MDE
galaxy10_mde = pymde.preserve_neighbors(X_train,embedding_dim=2,verbose=True).embed(verbose=True)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_mde[:, 0], galaxy10_mde[:, 1], c=y_train, cmap=plt.cm.nipy_spectral,
        edgecolor='k',label=y_train)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_pymde.svg")

### PACMAP
galaxy10_pacmap = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0).fit_transform(X_train, init="pca")
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_pacmap[:, 0], galaxy10_pacmap[:, 1], c=y_train, cmap=plt.cm.nipy_spectral,
        edgecolor='k',label=y_train)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_pacmap.svg")

### UMAP
reducer= umap.UMAP(n_components=2, n_neighbors=5,
   random_state=42, transform_seed=42, verbose=False)
reducer.fit(X_train)

galaxy10_umap = reducer.transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_umap[:, 0], galaxy10_umap[:, 1], c=y_train, cmap=plt.cm.nipy_spectral,
        edgecolor='k',label=y_train)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_umap.svg")

### UMAP - Supervised
reducer= umap.UMAP(n_components=2, n_neighbors=15,
   random_state=42, transform_seed=42, verbose=False)
reducer.fit(X_train,y_train)

galaxy10_umap_supervised = reducer.transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_umap_supervised[:, 0], galaxy10_umap_supervised[:, 1],
        c=y_train, cmap=plt.cm.nipy_spectral,edgecolor='k',label=y_train)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_umap_supervised.svg")

### UMAP - Supervised prediction
galaxy10_umap_supervised_prediction = reducer.transform(X_test)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(galaxy10_umap_supervised_prediction[:, 0], galaxy10_umap_supervised_prediction[:, 1],
        c=y_test, cmap=plt.cm.nipy_spectral,edgecolor='k',label=y_test)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_umap_supervised_prediction.svg")

## 3D Embedding
### PCA
pca = decomposition.PCA(n_components=3)
pca.fit(X_train)
galaxy10_pca = pca.transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_pca[:, 0], galaxy10_pca[:, 1],
               galaxy10_pca[:, 2], c=y_train,
               cmap=plt.cm.nipy_spectral, edgecolor='k',label=y_train)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_pca.svg")

### trimap
galaxy10_trimap = trimap.TRIMAP(n_dims=3).fit_transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_trimap[:, 0], galaxy10_trimap[:, 1],
                galaxy10_trimap[:, 2], c=y_train,
                cmap=plt.cm.nipy_spectral, edgecolor='k',label=y_train)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_trimap.svg")

### MDE
galaxy10_mde = pymde.preserve_neighbors(X_train,embedding_dim=3,verbose=True).embed(verbose=True)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_mde[:, 0], galaxy10_mde[:, 1],
               galaxy10_mde[:, 2], c=y_train,
               cmap=plt.cm.nipy_spectral, edgecolor='k',label=y_train)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_pymde.svg")

### PACMAP
galaxy10_pacmap = pacmap.PaCMAP(n_dims=3, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0).fit_transform(X_train, init="pca")
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_pacmap[:, 0], galaxy10_pacmap[:, 1],
               galaxy10_pacmap[:, 2], c=y_train,
               cmap=plt.cm.nipy_spectral, edgecolor='k',label=y_train)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_pacmap.svg")

### UMAP
reducer= umap.UMAP(n_components=3, n_neighbors=5,
   random_state=42, transform_seed=42, verbose=False)
reducer.fit(X_train)

galaxy10_umap = reducer.transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_umap[:, 0], galaxy10_umap[:, 1],
              galaxy10_umap[:, 2], c=y_train,
              cmap=plt.cm.nipy_spectral,edgecolor='k',label=y_train)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_umap.svg")

### UMAP - Supervised
reducer= umap.UMAP(n_components=3, n_neighbors=15,
   random_state=42, transform_seed=42, verbose=False)
reducer.fit(X_train,y_train)

galaxy10_umap_supervised = reducer.transform(X_train)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_umap_supervised[:, 0], galaxy10_umap_supervised[:, 1],
              galaxy10_umap_supervised[:, 2],c=y_train,
              cmap=plt.cm.nipy_spectral,edgecolor='k',label=y_train)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_umap_supervised.svg")

### UMAP - Supervised prediction

galaxy10_umap_supervised_prediction = reducer.transform(X_test)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
ax = fig.add_subplot(projection='3d')
p = ax.scatter(galaxy10_umap_supervised_prediction[:, 0], galaxy10_umap_supervised_prediction[:, 1],
              galaxy10_umap_supervised_prediction[:, 2],c=y_test,
              cmap=plt.cm.nipy_spectral,edgecolor='k',label=y_test)
fig.colorbar(p,ax=ax,boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_3D_umap_supervised_prediction.svg")




