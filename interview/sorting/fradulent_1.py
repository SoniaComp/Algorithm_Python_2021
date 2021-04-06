#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    check_list = sorted(expenditure[:d])
    if d % 2 == 0:
        for i, num in enumerate(expenditure[d:]):
            mid = check_list[d//2:d//2+2]
            if num >= sum(mid):
                count += 1
            check_list.remove(expenditure[i])
            idx = bisect_left(check_list, num)
            check_list.insert(idx, num)
    else:
        for i, num in enumerate(expenditure[d:]):
            mid = check_list[d//2]
            if num >= mid*2:
                count += 1
            check_list.remove(expenditure[i])
            idx = bisect_left(check_list, num)
            check_list.insert(idx, num)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
