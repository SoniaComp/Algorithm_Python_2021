#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    for idx, char in enumerate(s):
        sub_count = 1
        # odd
        left, right = idx, idx+1
        while left >= 0 and right < len(s):
            if s[left] == s[right] == s[idx]:
                sub_count+=1
                left, right = left-1, right+1
            else:
                break
            
        # even
        left, right = idx-1, idx+1
        while left >= 0 and right < len(s):
            if s[left] == s[right] == s[idx-1]:
                sub_count+=1
                left, right = left-1, right+1
            else:
                break
        count += sub_count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
