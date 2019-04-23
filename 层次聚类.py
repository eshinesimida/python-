# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:46:28 2019

@author: Administrator
"""

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle  ##python自带的迭代器模块

##产生随机数据的中心
centers = [[1, 1], [-1, -1], [1, -1]]
##产生的数据个数
n_samples=3000
##生产数据
X, lables_true = make_blobs(n_samples=n_samples, centers= centers, cluster_std=0.6, 
                  random_state =0)


##设置分层聚类函数
linkages = ['ward', 'average', 'complete']
n_clusters_ = 4
ac = AgglomerativeClustering(linkage=linkages[2],n_clusters = n_clusters_)
##训练数据
ac.fit(X)

##每个数据的分类
lables = ac.labels_

##绘图
plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    ##根据lables中的值是否等于k，重新组成一个True、False的数组
    my_members = lables == k
    ##X[my_members, 0] 取出my_members对应位置为True的值的横坐标
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()