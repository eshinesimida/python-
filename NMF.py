# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:04:56 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
#可视化
from sklearn import decomposition
#加载PCA算法包
from sklearn.datasets import fetch_olivetti_faces
from numpy.random import RandomState

n_row, n_col = 2, 3
n_components = n_row * n_col
#设置提取的特征数目
image_shape = (64, 64)
#设置人脸数据图片的大小 
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data

def plot_gallery(title, images, n_col = n_col, n_row = n_row):
    plt.figure(figsize = (2. * n_col, 2.26 * n_row))
    plt.suptitle(title, size = 16)
    
    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,
                   interpolation='nearest', vmin=-vmax, vmax=vmax)
        plt.xticks(())
        plt.yticks(())
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.)
 
     
plot_gallery("First centered Olivetti faces", faces[:n_components])

estimators = [
    ('Eigenfaces - PCA using randomized SVD',
         decomposition.PCA(n_components=6,whiten=True)),
 
    ('Non-negative components - NMF',
         decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3))
]
 
###############################################################################
 
for name, estimator in estimators:
    print("Extracting the top %d %s..." % (n_components, name))
    print(faces.shape)
    estimator.fit(faces)
    components_ = estimator.components_
    plot_gallery(name, components_[:n_components])
 
plt.show()
