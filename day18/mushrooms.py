# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
dataset = pd.read_csv('mushrooms.csv')  
features = dataset.iloc[:,[5,21,22]].values
labels = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,2] = labelencoder.fit_transform(features[:,2])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = np.delete(features,[0],axis=1)

onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = np.delete(features,[1],axis=1)

onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = np.delete(features,[2],axis=1)


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)



# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)


#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)
labels_pred = classifier.predict(features_test)

print(labels_pred)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

