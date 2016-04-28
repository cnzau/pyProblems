#!/usr/bin/python
import ast
"""Accepts as the first parameter a string specifying the data structure to be used 'list', 'set' or 'dictionary'
Accepts the second parameter the data to be manipulated based on the data structure specified e.g [1, 4, 9, 16, 25] for a list data structure
Based on the first parameter
  -return the reverse of a list or
  -add items in the global variables to the set and return the resulting set
  -return the keys of a dictionary
"""
st = raw_input('Enter type of data(list, set or dictionary): ')
dt = raw_input('Enter data to be manipulated: ')
# st = ast.literal_eval(st)
dt = ast.literal_eval(dt)

m = 'MORINGA'
h = 'IHUB'
l = 'ILAB'
def manipulate_data(sti, data):
    if sti == "list":
        data.reverse()
        return data
    elif sti == "set":
        data.add(m)
        data.add(h)
        data.add(l)
        return data
    elif sti == "dictionary":
        return data.keys()
    else:
        return 'data type not a list, set or a dictionary'

print manipulate_data(st, dt)
