# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = input()
s = input().split()
CN = int(input())
all_n = len(list(combinations(s, CN)))
not_a_n = len(list(combinations(list(filter(lambda x: x!='a', s)), CN)))
print((all_n - not_a_n) / all_n)