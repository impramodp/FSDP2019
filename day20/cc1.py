# -*- coding: utf-8 -*-
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  


dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter=" ")  

features = dataset.iloc[:, :8].values  
labels = dataset.iloc[:, -1].values 

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)
