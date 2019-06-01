# -*- coding: utf-8 -*-


"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""

l1=input("enter list1 numbers").split(",")
l2=input("enter list2 numbers" ).split(",")
set1=set(l1)
set2=set(l2)
set3=set2.intersection(set1)
print(list(set3))