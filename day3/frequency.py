# -*- coding: utf-8 -*-


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

user_input = input("Enter a String: ")

char_freq = {}      
for x in user_input:

    char_freq[x] = char_freq.get(x,0) + 1
    
print (char_freq)


