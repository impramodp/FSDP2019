# -*- coding: utf-8 -*-

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
file_name - 'copy_file.py'
"""
# copy 'words.txt' into 'abc.txt'

copy_file = open('abc.txt','wt')
with open('words.txt','rt') as file:
    for text in file.readlines():
        copy_file.write(text)
copy_file.close()