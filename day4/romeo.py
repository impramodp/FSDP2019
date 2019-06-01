
"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Letâ€™s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

# -*- coding: utf-8 -*-

with open("romeo.txt", "rt") as f:

    l = f.readlines()
    
    1l = []
    for x in l:
        l1.append(x.split())
    
    dict1 = {}
    for y in l1:
        for z in y:
            if z not in dict1:
                dict1[z] = 1
            else:
                dict1[z]+=1
