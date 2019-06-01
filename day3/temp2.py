# -*- coding: utf-8 -*-
l1 = ["eat","sleep","repeat"]    

index = 0
for ele in l1 :
  print("{} {} ". format (index, ele ))
  index += 1
  
for ele in enumerate(l1):      
    print (ele)  
    print (type(ele))
    names_of_days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )


for index, item in enumerate(names_of_days):
  print("{} : {} ". format (index, item ))
 

for step in enumerate(names_of_days):
  print("{} : {} ". format (step[0], step[1] ))
 

for step in enumerate(names_of_days):
    print("{} : {} ". format (*step))


def my_func():
    return (1,2,3)
 
my_func()

tup = my_func()
 
a,b,c = my_func()

print (a)
print (b)
print (c)



dict1 = dict({})  
print(type(dict1))
dict1['lname'] = 'Miller'
dict1['profession'] = 'electrician'
dict1['age'] = '36'
dict1['city'] = 'NY' #add
print(dict1)

dict1['city'] = 'MA' #update
print(dict1)

dict1.update ( {'age':32, 'city':'NY' } )
print(dict1)

# Printing Values
print (dict1["lname"])
print (dict1.get('lname'))
print (dict1.get('name'))
dict1 = {'fname':'John', 'lname':'Miller', 'profession':'plumber',  'age':'32'}


# To list all the keys
a  = dict1.keys()
print(a)
print(type(a)) 

# To list all the values  
print(dict1.values())


# To list all the values  
print(dict1.items())



# To list all keys  
for key in dict1.keys() :
  print ( key)


# To list all values   
for value in dict1.values():
  print ( value )

 
# To list all values and keys  
for key in dict1:
  print ( key , dict1[key] )

for key in dict1:
  print ( key , dict1.get(key) )



