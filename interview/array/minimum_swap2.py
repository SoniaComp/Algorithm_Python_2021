#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    arr = [0] + arr
    tmp = [0] * len(arr)
    for idx, num in enumerate(arr):
        tmp[num] = idx
    for i in range(len(arr)):
        if i != arr[i]:
            count += 1
            change = tmp[i]
            arr[i], arr[change] = i, arr[i]
            tmp[i], tmp[arr[change]] = i, change
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
