# -*- coding: utf-8 -
"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the dataset
dataset = pd.read_csv('iq_size.Csv')
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0:1].values


# Building the optimal model using Backward Elimination
import statsmodels.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.
features = sm.add_constant(features)



features_opt = features[:, [0,1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0,1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
#regressor_OLS.pvalues
features_opt = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

dataset.plot(x='Brain', y='PIQ', style='o')  
plt.title('Brain size vs piq')  
plt.xlabel('Brain')  
plt.ylabel('PIQ')  
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 6)
features_poly = poly_object.fit_transform(features_opt)


from sklearn.linear_model import LinearRegression  

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)



plt.scatter(features_opt, labels, color = 'red')
plt.plot(features_opt, lin_reg_2.predict(poly_object.fit_transform(features_opt)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Brainsize')
plt.ylabel('Piq')
plt.show()

print("Predicting result with Polynomial Regression for brain size=90")
print(lin_reg_2.predict(poly_object.transform(np.reshape(90,(1,-1)))))




"""when we pass all three parameters as features

"""

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 6)
features_poly = poly_object.fit_transform(features)


from sklearn.linear_model import LinearRegression  

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)



plt.scatter(features_opt, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Brainsize')
plt.ylabel('Piq')
plt.show()

print("Predicting result with Polynomial Regression for brain size=90")
list1=np.array([90,70,150])
list1=list1.reshape(1,-1)
print(lin_reg_2.predict(list1)

