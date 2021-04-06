#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=lambda x: (-x[1], x[0]))
    loose_count = len(list(filter(lambda x: x[1]==1, contests))) - k
    sum_count = 0
    for contest in contests[loose_count:]:
        sum_count += contest[0]
    for contest in contests[:loose_count]:
        sum_count -= contest[0]
    return sum_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
