# -*- coding: utf-8 -*-


student_data = []

while True:
    user_input = input("Enter name, age and score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    
    student_data.append( (name, int(age), int(marks) ) )

student_data.sort()
print (student_data)
