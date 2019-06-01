# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


df = pd.read_csv("Telecom_churn.csv")
df_1= df[df[(df['international plan']==True) & (df['voice mail plan']==True)&(df['churn']==True)]]

print(df_1)
df_2=df['total intl charge'][df['churn'] == True ]
df_3=df['total intl charge'][df['churn'] == False]
print(df_2)
print(df_3)
y=np.array(df_2)
z=np.array(df_3)
sum1=0
for value1 in y:
    sum1+=value1
sum2=0
for value2 in y:
    sum2+=value2
print("total charge for international calls",sum1+sum2)    

df_4=df[df['churn'] == True ]
df_4["state"][df_4["total night minutes"]==df_4["total night minutes"].max()]
