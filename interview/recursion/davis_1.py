#!/bin/python3
# 재귀를 사용해도 글로벌 변수를 토앻서, 
import math
import os
import random
import re
import sys
from collections import defaultdict

def stepPerms(n):
        if memo[n] != 0:
            return memo[n]
        memo[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
        return memo[n]
    
if __name__ == '__main__':
    global memo
    memo = defaultdict(int)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()