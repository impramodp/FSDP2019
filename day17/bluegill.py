# -*- coding: utf-8 -*-
"""
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the dataset
dataset = pd.read_csv('bluegills.Csv')
features = dataset.iloc[:,:1].values
labels = dataset.iloc[:, 1].values

dataset.plot(x='age', y='length', style='o')  
plt.title('age vs length')  
plt.xlabel('age')  
plt.ylabel('length')  
plt.show()
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)

from sklearn.linear_model import LinearRegression  

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)



plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

print("Predicting result with Polynomial Regression for age=5")
print(lin_reg_2.predict(poly_object.transform(np.reshape(5,(1,-1)))))

