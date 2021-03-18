#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the whatFlavors function below.
# 숫자가 크기 때문에 1초 1억(0이 8개)
def whatFlavors(costs, money):
    flavor_costs = defaultdict(list)
    
    for i, cost in enumerate(costs):
        flavor_costs[cost].append(i+1)
    
    for cost in flavor_costs:
        if (money - cost) in flavor_costs:
            if money - cost == cost and len(flavor_costs[cost]) >= 2:
                print(' '.join(map(str, flavor_costs[cost][:2])))
                return
            elif money - cost != cost:
                print(str(flavor_costs[cost][0]) + ' ' + str(flavor_costs[money-cost][0]))
                return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
