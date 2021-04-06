#!/bin/python3
# greedy 한 해법
import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    d = {}
    for i in arr:
        d[i] = i
    for j in arr:
        g = j + k
        if g in d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
