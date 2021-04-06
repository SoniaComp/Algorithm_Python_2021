#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    arr.sort()
    left, right = 0, 1
    while right < len(arr) and left < len(arr):
        diff = arr[right] - arr[left]
        if diff > k:
            left += 1
        elif diff < k:
            right += 1
        else:
            count += 1
            left += 1
            right += 1
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
