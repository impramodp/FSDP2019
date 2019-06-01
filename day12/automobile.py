# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())
x=df['price']
print(x)
y=np.array(x)
print(y)
print("maximum price:",y.max())
print("minimum price:",y.min())
print("standard deviation:",np.std(y))
