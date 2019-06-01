# -*- coding: utf-8 -*-
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""


user_input = input("enter name of days of week:").split(",")
#user_input = tuple(user_input)
tuple2=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for var in tuple2:
    if var not in user_input:
      user_input.append(var)
print(tuple(user_input))     