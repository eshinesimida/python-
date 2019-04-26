# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:32:21 2019

@author: Administrator
"""

from sklearn.neighbors import KNeighborsClassifier

X = [[0],[1],[2],[3]]
y = [0,0,1,1]
neigh = KNeighborsClassifier(n_neighbors = 3)
neigh.fit(X,y)

print(neigh.predict([[4.1]]))


