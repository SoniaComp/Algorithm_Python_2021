#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    dp = [1]*n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
    
    for j in range(n-1, 0, -1):
      if arr[j] < arr[j-1] and dp[j] >= dp[j-1]:
        dp[j-1] = dp[j] + 1
    
    return sum(dp)

                    
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
