# -*- coding: utf-8 -*-

"""
Code Challenge
  Name: 
    Different sizes
  Filename: 
    png.py
  Problem Statement:
    Convert all files PNG in a directory into different sizes
  Hint: 
    os.listdir('.') function will list all the files in the current directory   
"""


import os
from PIL import Image

for f in os.listdir('.') :
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, text = os.path.splittext(f)
        i.save('pngs/{}.png'.format(fn))
 

""" 
Resize the images for web Development in a directory for thumbnail 
or image gallery ( maintain aspect ratio ) 
"""

size_300 = (300,300)
size_700 = (700,700)


for f in os.listdir('.') :
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)
        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))
 
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))
