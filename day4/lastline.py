# -*- coding: utf-8 -*-

filename = input("Enter a filename: ")
print(open(filename).readlines()[-1])
 
for line in open(filename):
    print(len(line))
 
 
for line in open(filename):
    pass
