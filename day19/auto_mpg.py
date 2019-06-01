# -*- coding: utf-8 -*-

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  


columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
dataset = pd.read_csv("Auto_mpg.txt",delimiter="\s+",names=columns)  


dataset['horsepower'].isnull()
dataset['horsepower']=dataset['horsepower'].replace("?",140)
dataset["horsepower"] = dataset["horsepower"].astype("float64")
features = dataset.iloc[:,1:8].values  
labels = dataset.iloc[:, 0].values  


print("highest mpg value",dataset["mpg"].max())

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeRegressor  
regressor1 = DecisionTreeRegressor()  
regressor1.fit(features_train, labels_train)  

labels_pred = regressor1.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
print(df)

list1=[6,215,100,2630,22.2,80,3]
list1= np.array(list1)
list1=list1.reshape(1,-1)
labels_pred = regressor1.predict(list1)

print(labels_pred)

"""random forest"""

#train the model
from sklearn.ensemble import RandomForestRegressor

regressor2 = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor2.fit(features_train, labels_train)  
labels_pred = regressor2.predict(features_test)  
dr=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
print(dr)

list2=[6,215,100,2630,22.2,80,3]
list2= np.array(list1)
list2=list2.reshape(1,-1)
labels_pred = regressor2.predict(list2)

print(labels_pred)
