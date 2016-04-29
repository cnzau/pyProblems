#!/usr/bin/python
def mySum(a, b, c, d, *args):
    """ function that find sum of atleast 4 required argument plus any other"""
    result = a + b + c + d
    if len(args) < 1:
        return result
    elif len(args) == 1:
        return result + args[0]
    else:
        for arg in args:
            result += arg
        return result
        # def argSum(*args):
        # 	"""function for summaton if arguments > 1"""
        #     return result + args[-1] + argSum(*args[:-1])
    # print args[-1]
    # print args[:-1]
    # print args
    # print "done"
