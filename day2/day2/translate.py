# -*- coding: utf-8 -*-

str=input("enter a string")
def translate(s1):
    l1=[]
    constant='bcdfghjklmnpqrstvwxyz'

    for i in s1:
        if i in constant:
            l1.append(i+'o'+i)
        else:
            l1.append(i)
    s2="".join(l1)
    print(s2)    

translate(str)       