'''
blueprint
lambda argument: manipulate(argument)
'''
def add(x, y): return x + y


print(add(3, 5))
# Output: 8

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
list1 = [1, 2]
list2 = [3, 4]
data = zip(list1, list2)
data = sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
