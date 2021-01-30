# 1. 인스턴스와 클래스 차이 이해하기
'''
Instance variables are for data which is unique to every object
Class variables are for data shared between different instances of a class
'''

# 2. new style classes
'''
- Old base classes do not inherit from anything
- New style base classes inherit from object
'''
class OldClass():
    def __init__(self):
        print('I am an old class')

class NewClass(object):
    def __init__(self):
        print('I am a jazzy new class')

old = OldClass()
# Output: I am an old class

new = NewClass()
# Output: I am a jazzy new class

'''
 A major advantage is that you can employ some useful optimizations like __slots__. You can use super() and descriptors and the likes. 
'''

# 3. method
# __init__
# __getitem__: Implementing getitem in a class allows its instances to use the [] (indexer) operator.
class GetTest(object):
    def __init__(self):
        self.info = {
            'name':'Yasoob',
            'country':'Pakistan',
            'number':12345812
        }

    def __getitem__(self,i):
        return self.info[i]

foo = GetTest()

foo['name']
# Output: 'Yasoob'

foo['number']
# Output: 12345812

'''
Without the __getitem__ method we would have got this error:
>>> foo['name']

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'GetTest' object has no attribute '__getitem__'
'''
