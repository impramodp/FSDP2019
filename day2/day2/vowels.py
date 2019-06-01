# -*- coding: utf-8 -*-

"""states=['Albama','California','Oklahoma','Florida']
vowels=list('aeiou')
new_list=[]
for x in states:
    
    
    for e in vowels:
        while e in x:
            l1= list(x)
            l1.remove(e)
            new_list.append("".join(l1))

print(new_list)
"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list('aeiou')

final_list = []

for state in state_name:
    state_elements = list(state.lower())
    
    for element in vowels:
        while element in state_elements:
            state_elements.remove(element)
    final_list.append("".join(state_elements))

print (final_list)
