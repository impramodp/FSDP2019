# -*- coding: utf-8 -*-
"""Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt



wiki="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")


all_tables=soup.find_all('table')


right_table=soup.find('table', class_='wikitable')

print (right_table)
A=[]
B=[]
C=[]
for row in right_table.findAll('tr'):
    states = row.findAll('td')
    if len(states) == 7:
        A.append(states[1].text.strip())
        B.append(states[2].text.strip())
        C.append(states[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Area","national share"]
col_data = OrderedDict(zip(col_name,[A,B,C]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
print(df[0:6])
labels = ["rajasthan"," mp"," maharashtra", "up", "gujrat", "karnataka"]
sizes = [10.41,9.37,9.36,7.33,5.96,5.83]

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan','pink']
explode = (0.1, 0, 0, 0, 0, 0)  
 #explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)


plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

 