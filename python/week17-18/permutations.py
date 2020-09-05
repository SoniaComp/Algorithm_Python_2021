from itertools import permutations, combinations

# 순열
a = [1,2,3]
permute = permutations(a, 2)
print(permute) #<itertools.permutations object at 0x7ffd1da0e8e0>
print(list(permute)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 조합
combi = combinations(a,2)
print(list(combi)) #[(1, 2), (1, 3), (2, 3)]