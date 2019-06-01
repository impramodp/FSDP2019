# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('affairs.csv')
features =dataset.iloc[:,:8].values
labels =dataset.iloc[:,8].values 

#on ehot encoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# Avoiding the Dummy Variable Trap
features = np.delete(features,[0,6],axis=1)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)



# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)



probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

print (pd.DataFrame(labels_pred, labels_test))


# Prediction for a new values 
# make this accorifng to the data csv
# Development is replaced by 1,0,0 to 0,0 to remove dummy trap


s = [3,25,3,1,4,16,4,2]
s= np.array(s)
s=s.reshape(1,-1)
a=onehotencoder.transform(s).toarray()
a = np.delete(a,[0,6],axis=1)
p = classifier.predict_proba(a)
p
p = (p>0.7)
print(p)
labels_pred = classifier.predict(a)
print(labels_pred)
