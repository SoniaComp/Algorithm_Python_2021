#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def isEqual(a, b):
    return a==b or a.upper()==b

def abbreviation(a, b):
    A_LEN = len(a)
    B_LEN = len(b)
    DP = [[False]*B_LEN for _ in range(A_LEN)]
    DP[0][0] = isEqual(a[0], b[0]) or a[0].islower()
    for i in range(1, A_LEN):
        for j in range(B_LEN):
            if j >= 0 and DP[i-1][j-1] and isEqual(a[i], b[j]):
                DP[i][j] = True
            if DP[i-1][j] and a[i].islower():
                DP[i][j] = True
    return "YES" if DP[A_LEN-1][B_LEN-1] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
