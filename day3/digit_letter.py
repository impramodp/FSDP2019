# -*- coding: utf-8 -*-
"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the Letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

from collections import OrderedDict 
user_input = input("Enter a string : ")

od = OrderedDict() 
od["Digits"] = 0
od["Letters"] = 0


for character in user_input:    
    if character.isalpha():    
        od["Letters"] = od["Letters"] + 1 
    elif character.isdigit():           
        od["Digits"] = od["Digits"] + 1 
            
for key, value in od.items() :
  print ( key, value )
