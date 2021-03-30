#!/bin/python3

import math
import os
import random
import re
import sys

# brackets = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }
# Complete the isBalanced function below.


def isBalanced(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    # for char in s:
    #     if char in brackets:
    #         if not stack:
    #             return 'NO'
    #         if len(stack) and brackets[char] != stack.pop():
    #             return 'NO'
    #     else:
    #         stack.append(char)
    for char in s:
        # if not stack:
        #   stack.append(char)
        # elif char not in table:
        #   stack.append(char)
        # elif table[char] == stack[-1]:
        #   stack.pop()
        if char in table:
            if not stack or table[char] != stack.pop():
                return "NO"
        else:
            stack.append(char)
    if stack:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
