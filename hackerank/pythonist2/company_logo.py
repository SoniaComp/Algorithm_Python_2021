#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    s_counts = sorted([(-count, k) for k, count in Counter(s).items()])
    for char in s_counts[:3]:
        print(f'{char[1]} {-char[0]}')