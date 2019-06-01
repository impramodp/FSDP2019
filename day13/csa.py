# -*- coding: utf-8 -*-
"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""

import pandas as pd
import matplotlib.pyplot as plt
df1=pd.DataFrame(columns=['Name','sex','Number','year'])
for i in range(1880,2010):
    filename="yob"+str(i)+".txt"
    df2=pd.read_csv(filename,header=None)
    df2.columns=['Name','sex','Number']

