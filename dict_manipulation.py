#!/usr/bin/python
#dictionary with key: value pair
def dict_manipulate():
    """Create a dictonary with key: value set, name: moringa school.
        Loop. If it finds name change to  Moringa. Reason for loop. Do it in a function.
    """
    #dictionary
    school = {'country': 'Kenya', 'category': 'code school', 'name': 'Moringa School'}
    #prints the keys as a list
    print "The keys are:"
    print school.keys()
    print "The original dictionary was:"
    print school
    #for loop to loop through every key in dictionary. if key name is found its value is changed
    for key in school.keys():
        if key == 'name':
            school['name'] = 'Moringa'
    print "manipulated to"
    print school

print dict_manipulate();
