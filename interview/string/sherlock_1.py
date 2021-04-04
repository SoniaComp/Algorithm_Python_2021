'''
TestCase를 보고 예외처리함
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    items = Counter(s)
    counts = [items[item] for item in items]
    if len(set(counts)) > 2:
        return 'NO'
    if len(set(counts)) == 1:
        return 'YES'
    if len(set(counts)) == 2:
        counts.sort(reverse=True)
        if counts[0] != counts[1]:
            return 'YES' if counts[0] - counts[1] == 1 else 'NO'
        else:
            return 'YES' if counts[-1] == 1 and counts[0] == counts[-2] else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
