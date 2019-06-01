# -*- coding: utf-8 -*-
import pandas as pd
reviews = pd.read_csv("ign.csv")
xb=(df['score']>7)&(df['platform']=="Xbox One")
x=xb.value_counts()
print("xbox one score is >7 :",x[1])
ps=(df['platform']=="PlayStation 4")
print(ps)
p=ps.value_counts()
q=(df['platform']=="Xbox One")
q=q.value_counts()
q[1]

p[1]

xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist", legend=True)
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist", legend=True)
filtered_reviews["score"].plot(kind="hist", legend=True)
