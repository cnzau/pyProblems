#!/usr/bin/python
"""Accepts as the first parameter a string specifying the data structure to be used 'list', 'set' or 'dictionary'
Accepts the second parameter the data to be manipulated based on the data structure specified e.g [1, 4, 9, 16, 25] for a list data structure
Based on the first parameter
  -return the reverse of a list or
  -add items in the global variables to the set and return the resulting set
  -return the keys of a dictionary
"""

m = 'MORINGA'
h = 'IHUB'
l = 'ILAB'
def manipulate_data(string, data):
    if string == "list":
        data.reverse()
        return data
    elif string == "set":
        data.add(m)
        data.add(h)
        data.add(l)
        return data
    elif string == "dictionary":
        return data.keys()
    else:
        return 'data type not a list, set or a dictionary'

print manipulate_data(st, dt)
