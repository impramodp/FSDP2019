# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Automobile.csv")
series=df["make"].value_counts()
print(series.index[0:11])
print(series.values[0:11])
explode = (0.1,0,0,0,0,0,0,0,0,0,0)
plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11])
plt.axis('equal')  
plt.show()
