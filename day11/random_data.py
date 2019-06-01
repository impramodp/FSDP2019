# -*- coding: utf-8 -*-
"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

"""
import numpy as np
from collections import Counter
x=np.random.randint(5,15,40)
print(x)
y=Counter(x)
print(y)
z=y.most_common()[0][0]
print(z)"""
import numpy as np

x=np.random.randint(5,15,40)
print(x)

print("most frequent value: :",np.bincount(x).argmax())
