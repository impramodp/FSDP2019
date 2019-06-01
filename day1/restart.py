# -*- coding: utf-8 -*-

str1=input("enter a string")
replaced_char=input("enter the character you want to replace")
replacement_char=input("enter char eith younwant to replace")
#first appearence of replaced char
f_occur=str1.find(replaced_char)
str2=str1[:f_occur+1] 
str3=str1[f_occur+1:].replace(replaced_char, replacement_char,)
str4=str2+str3
print(str4)
