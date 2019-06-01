# -*- coding: utf-8 -*-

user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    