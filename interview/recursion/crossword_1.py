#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
R = 0 # row
H = 1 # column
def back(start, d, length, finds):
    x, y = start
    if d == R:
        for i in range(length):
            finds[x+i][y] = 0
    else:
        for i in range(length):
            finds[x][y+i] = 0        
            
def find(start, d, word, finds):
    x, y = start
    if d == R:
        for i in range(len(word)):
            finds[x+i][y] = word[i]
    else:
        for i in range(len(word)):  
            finds[x][y+i] = word[i] 

def crosswordPuzzle(crossword, words):
    words = words.split(';')
    finds = [[0]*10 for _ in range(10)]
    points = []
    for i in range(10):
        for j in range(10):
            if crossword[i][j] == '-' and not find[i][j]:
                points.append([i, j])
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    finds = input()

    result = crosswordPuzzle(crossword, finds)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
