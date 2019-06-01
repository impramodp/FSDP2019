# -*- coding: utf-8 -*-= 
str=input("Enter the string :")
l1=[]
count=0
for i in str:
    l1.append(i)
final_list=[]
for y in l1:
      if y not in final_list:
          final_list.append(y)
for elements in final_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
if count == 26:
    print ("Pangram")
else:
    print ("Not Pangram")
              