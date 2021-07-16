from collections import Counter

def solution1(n, k):
  return list(map(lambda x: x[0], Counter(n).most_common(k)))

# test 
# from random import randint 
# arr = [randint(1, 100) for i in range(1000)] 
# solution1(arr, 10)