#Everything in Python is an object and we can examine those objects. Python ships with a few built-in functions and modules to help us.
'''
1. dir
It returns a list of attributes and methods belonging to an object. 
If we run dir() without any argument then it returns all names in the current scope.

2. type, id
The type function returns the type of an object. 
id returns the unique ids of various objects

3. inspect
The inspect module also provides several useful functions to get information about live objects.
'''

my_list = [1, 2, 3]
dir(my_list)
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... .