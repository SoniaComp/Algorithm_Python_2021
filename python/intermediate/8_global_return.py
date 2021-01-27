from collections import namedtuple


def add(value1, value2):
    r = value1 + value2


add(2, 4)
# print(result)

# Oh crap, we encountered an exception. Why is it so?
# the python interpreter is telling us that we do not
# have any variable with the name of result. It is so
# because the result variable is only accessible inside
# the function in which it is created if it is not global.
# Traceback (most recent call last):
#   File "", line 1, in
#     result
# NameError: name 'result' is not defined

# Now lets run the same code but after making the result
# variable global


def add(value1, value2):
    global result
    result = value1 + value2


def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)


# Use as namedtuple
p = profile()
print(p, type(p))
# Person(name='Danny', age=31) <class '__main__.Person'>
print(p.name)
# Danny
print(p.age)
# 31

# Use as plain tuple
p = profile()
print(p[0])
# Danny
print(p[1])
# 31

# Unpack it immediatly
name, age = profile()
print(name)
# Danny
print(age)
# 31
