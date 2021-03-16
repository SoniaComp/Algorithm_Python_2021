#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    # abba
    # count = []
    count = 0
    for i in range(1, len(s)+1): 
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)] 
        b = Counter(a)
        # 3일때는 3을 2쌍식 조합으로 나누는 거니까 아래식.. 헐... 대박..
        # count.append(sum([len(list(combinations(['a']*b[j], 2))) for j in b]))
        for key in b:
          count += (b[key] ** 2 - b[key]) / 2 if b[key] >= 2 else 0
    # sonia style
    # count = 0
    # for i in range(1,len(s)+1):
    #     a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
    #     b = Counter(a)

    #     count += sum([int((b[key] ** 2 - b[key]) / 2) for key in b if b[key] >= 2])
    return sum(count)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
