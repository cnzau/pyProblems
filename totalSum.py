#!/usr/bin/python
def totalSum(*args):
    """ function that takes in numbers and prints their total sum"""
    if len(args) < 1:
        return "Invalid! \nNo number entered."
    elif len(args) == 1:
        return args[0]
    else:
    	return args[-1] + totalSum(*args[:-1])

print totalSum()
print totalSum(0)
print totalSum(5)
print totalSum(5,7)
print totalSum(9, 6, 3)
print totalSum(7, 4, 2, 8)
print totalSum(5, 5, 7, 9, 7, 4, 1, 2, 3, 8)
