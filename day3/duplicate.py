# -*- coding: utf-8 -*-

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""


#l1=input("enter a list").split(",")
l1=[12,24,24,35,24,88,120,155,88,120,155,12]
s1=set(l1)
l2=list(s1)
print("list after removing duplicate values:",print(l2))
