#!/usr/bin/python
def list_manipulate():
    """list manipulation operations"""
    #creating a list
    l = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green']
    print l

    #ACCESS / INDEXING
    #1st item in list
    print l[0]
    #2st item in list
    print l[1]
    #last item in list
    print l[-1]

    #SLICING
    print l[1:4]
    #['orange', 'yellow', 'green']
    print l[2:]
    #['yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green']
    print l[:2]
    #['red', 'orange']
    print l[-1]
    #green
    print l[1:-1]
    #['orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue']

    #LENGTH. No of items in a list
    print len(l)
    #9

    #Sorting
    print sorted(l)
    #['Blue', 'black', 'blue', 'green', 'green', 'indigo', 'orange', 'red', 'yellow']

    #Append
    l.append('violet')
    print l[-1]
    #violet

    #Insert
    l.insert(0, 'white')
    print l
    #['white', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green', 'violet']
        
    
    #Remove item with value white
    l.remove('white')
    print l
    #['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green', 'violet']
    
    #EXTEND - grow list
    l2 = ['maroon', 'colors']
    l.extend(l2)
    print l2
    #['maroon', 'colors']
    print l
    #['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green', 'violet', 'maroon', 'colors']

    #DELETE - Remove an item from a list given its index instead of its value
    del l[-1]
    print l
    #['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green', 'violet', 'maroon']
    
    #POP - Remove last item in the list
    print l.pop()
    #maroon
    print l
    #['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'black', 'Blue', 'green', 'violet']
    
    #REVERSE
    l.reverse()
    print l
    #['violet', 'green', 'Blue', 'black', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    

    #COUNT
    print l.count('green')
    #2


    #Keyword in - if item is in list
    if 'green' in l:
        g = l.count('green')
        print 'list contains %d green items' %g
        #list contains 2 green items

    
    #for-in statement - makes it easy to loop over the items in a list
    for item in l2:
        print item
        #maroon
        #colors
    


list_manipulate();