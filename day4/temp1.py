# -*- coding: utf-8 -*-

file = open("words.txt", "rt")

position = file.tell()
print (position)

line = file.readline()
print (line )
