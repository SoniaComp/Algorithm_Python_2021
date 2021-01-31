'''
Context managers allow you to allocate and release resources precisely when you want to. The most widely used example of context managers is the with statement. Suppose you have two related operations which you’d like to execute as a pair, with a block of code in between. Context managers allow you to do specifically that. 
'''

'''While comparing it to the first example we can see that a lot of boilerplate code is eliminated just by using with. The main advantage of using a with statement is that it makes sure our file is closed without paying attention to how the nested block exits.'''

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with open_file('some_file') as f:
    f.write('hola!')