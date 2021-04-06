#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the maxCircle function below.
def maxCircle(queries):
    results = []
    new_num = 1
    group = defaultdict(list)
    people = defaultdict(int)
    max_value = 2
    
    for a, b in queries:
        if not people[a] and not people[b]:
            group[new_num] = [a, b]
            people[a] = people[b] = new_num
            new_num += 1
        elif people[a] and not people[b]:
            group_num = people[a]
            people[b] = group_num
            group[group_num].append(b)
            max_value = max(max_value, len(group[group_num]))
        elif people[b] and not people[a]:
            group_num = people[b]
            people[a] = group_num
            group[group_num].append(a)
            max_value = max(max_value, len(group[group_num]))
        else:
            group_a = people[a]
            group_b = people[b]
            if not group_a == group_b:
                if len(group[group_a]) >= len(group[group_b]):
                    group[group_a].extend(group[group_b])
                    for p in group[group_b]:
                        people[p] = group_a
                    max_value = max(max_value, len(group[group_a]))
                    del group[group_b]
                else:
                    group[group_b].extend(group[group_a])
                    for p in group[group_a]:
                        people[p] = group_b
                    max_value = max(max_value, len(group[group_b]))
                    del group[group_a]   
        results.append(max_value)
        
    return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
