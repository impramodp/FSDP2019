# -*- coding: utf-8 -*-
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""

# Importing the dataset
dataset = pd.read_csv('Female_Stats.Csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)
import statsmodels.api as sm
features = sm.add_constant(features)







features_opt = features[:, 1:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor.coef_


features_opt = features[:, 1]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor.coef_
