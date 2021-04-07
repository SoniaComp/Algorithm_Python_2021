import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [i-1 for i in q]  # set queue to start at 0
    bribes = 0
    
    for origin, cur in enumerate(q): # original, curr
        if cur - origin > 2:
            print('Too chaotic')
            return
        # print(cur)
        # print(origin)
        # print(q[max(cur-1, 0): origin])
        for k in q[max(cur-1, 0): origin]:
            if k > cur:
                bribes += 1

    print(bribes)
