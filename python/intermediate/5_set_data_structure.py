some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = set([x for x in some_list if some_list.count(x) > 1])

# 교집합
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

# 차집합
print(input_set.difference(valid))


