# -*- coding: utf-8 -*-
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

file = open('students.txt','w')
file.close()

with open('students.txt','a') as file:
    for i in range(25):
        absent_student_name = input("Enter the absent student name: ")
        if absent_student_name=="":
            break
        else:
         file.write(absent_student_name+'\n')
        

file = open('students.txt','r')
print(file.readlines())
