# -*- coding: utf-8 -*-


user_input=(input("enter the numbers: ")).split(" ")

def add(l1):
    s=0
    for i in l1:
       s+=i
    return(s)

def multiply(l1):
    multi=1
    for i in l1:
        multi*=i
    return(multi)
def largest(l1):
    return(max(l1))
def smallest(l1):
    return(min(l1))
def sorting(l1):
    return((l1.sort))
    print("hello")
def remove_duplicates(l1):
    e_list = []
    for i in l1:
        if i not in e_list:
            e_list.append(i)
    return e_list
def Print(l1):
    
    print(add(l1))
    print(multiply(l1))
    print(largest(l1))
    print(smallest(l1))
    print(sorting(l1))
    print(remove_duplicates(l1))


    
user_input=(input("enter the numbers: ")).split(" ")
list1=[]
for x in user_input:
    list1.append(int(x))
print (list1)     
