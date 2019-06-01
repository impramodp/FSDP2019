# -*- coding: utf-8 -*-



"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""



import numpy as np
import matplotlib.pyplot as plt
amounts = np.random.normal(150.0, 20.0, 1000)
print (amounts)
 
y=np.mean(amounts)
print("mean:",y)
z=np.median(amounts)
print("median:",z)
import matplotlib.pyplot as plt
plt.hist(amounts, 100)
plt.show()      
print("Standard Deviation is: ", np.std(amounts))
print("np.var:",np.var(amounts))