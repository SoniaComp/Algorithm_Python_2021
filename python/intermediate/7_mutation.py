
'''
 This is only true for mutable datatypes. Here is a gotcha involving functions and mutable data types:
'''
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [2]

add_to(3)
# Output: [3]
'''
Well again it is the mutability of lists which causes this pain. In Python the default arguments are evaluated once when the function is defined, not each time the function is called. You should never define default arguments of mutable type unless you know what you are doing. You should do something like this:
'''
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target