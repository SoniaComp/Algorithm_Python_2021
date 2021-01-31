'''
 In that case you have two choices. The first one is to distribute 2 modules, one for Python 2 and the other for Python 3. The other choice is to modify your current code and make it compatible with both Python 2 and 3.
'''

# The first and most important method is to use __future__ imports. It allows you to import Python 3 functionality in Python 2. 
print
# Output:

from __future__ import print_function
print(print)
# Output: <built-in function print>

try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2
  
  '''
  Now whenever you try to use the modules which are abandoned in Python 3, it raises a NameError like this:

from future.builtins.disabled import *

apply()
# Output: NameError: obsolete Python 2 builtin apply is disabled
External standard-library backports

There are a few packages in the wild which provide Python 3 functionality in Python 2. For instance, we have:

enum pip install enum34
singledispatch pip install singledispatch
pathlib pip install pathlib
'''

