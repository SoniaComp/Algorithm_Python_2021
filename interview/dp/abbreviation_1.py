#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    if len(b) > len(a):
        return 'NO'
    if len(b) == len(a):
        a = a.upper()
        return 'YES' if a == b else 'NO'
    
    ap = bp = 0
    while ap < len(a):
        if bp < len(b) and (a[ap] == b[bp] or a[ap].upper() == b[bp]):
            ap += 1
            bp += 1
        elif a[ap].islower():
            ap += 1
        else:
            break
    return 'YES' if bp == len(b)-1 and ap == len(a) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
