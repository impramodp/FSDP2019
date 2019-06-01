# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("training_titanic.csv")
df['Survived']
df['Survived'].value_counts()[1]
print("survived : ",df['Survived'].value_counts()[1])
print("died : ",df['Survived'].value_counts()[0])
print("survival rate :",df['Survived'].value_counts(normalize = True)[1]*100)
df_male = df['Survived'][df['Sex'] == 'male' ].value_counts()[1]
df_female=df['Survived'][df['Sex']=='female' ].value_counts()[1]
t_survived=df_male+df_female
m_vs_f=df_male/t_survived
f_vs_m=df_female/t_survived
print("male vs female survival",m_vs_f*100)
print("female vs male survival",f_vs_m*100)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df["child"]= df["Age"].map(lambda x: 0 if x>18  else 1 )
df