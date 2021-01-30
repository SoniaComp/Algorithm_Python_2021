# one-liner Python commands

# 1. simple web server
'''
# Python 2
python -m SimpleHTTPServer

# Python 3
python -m http.server
'''

# 2.pretty printing
import itertools
from pprint import pprint

my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
print(dir(my_dict))
pprint(dir(my_dict))

# cat file.json | python -m json.tool

# 3. profiling a script
# python -m cProfile my_script.py

# 4. CSV to json
# python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

# 5. list flattening
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
# Output: [1, 2, 3, 4, 5, 6]

# or
print(list(itertools.chain(*a_list)))
# Output: [1, 2, 3, 4, 5, 6]

# 6. One-Line Constructors
''' 
avoid boilerplate assignments
'''


class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update(
            {k: v for k, v in locals().items() if k != 'self'})

'''
레퍼런스: https://wiki.python.org/moin/Powerful%20Python%20One-Liners
'''