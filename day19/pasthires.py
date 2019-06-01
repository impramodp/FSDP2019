# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('PastHires.csv')
features =dataset.iloc[:,:6].values
labels =dataset.iloc[:,6].values 


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,3] = labelencoder.fit_transform(features[:,3])
features[:,4] = labelencoder.fit_transform(features[:,4])
features[:,5] = labelencoder.fit_transform(features[:,5])


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 
print(labels_pred)
#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

"""with random forest"""

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)


#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))

list1=[10,1,4,0,1,0]
list1= np.array(list1)
list1=list1.reshape(1,-1)
labels_pred = classifier.predict(list1)

print("hired or not: ",labels_pred)


