#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    dp = [0]*n
    dp[0] = 1
    pivot = 0
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
            pivot = i
        else:
            dp[i] = 1
            if pivot + 1 < i:
                for idx in range(i-1, pivot, -1):
                    dp[idx] = dp[idx+1] + 1
                if dp[pivot] < dp[pivot+1]:
                    dp[pivot] = dp[pivot+1] + 1
                    
    print(dp)
    return sum(dp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
