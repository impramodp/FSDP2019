# -*- coding: utf-8 -*-

str=input("enter a string")
l1=[]
def reverse(s1):
    r_str=" "

    for i in s1:
        l1.append(i)
        l2=l1[::-1]
    for x in l2:
        r_str=r_str+x
    print(r_str)
reverse(str)      