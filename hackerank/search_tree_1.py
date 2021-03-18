#!/bin/python3

import os
import sys

# sys.setrecursionlimit(2000)

from collections import deque

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.depth = 1

class Tree(object):
    def __init__(self):
        self.root = Node(1)

    def create_tree(self, data):
        queue = deque()
        data.reverse()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            left, right = data.pop()
            if left != -1:
                node.left = Node(left)
                node.left.depth = node.depth + 1
                queue.append(node.left)
            if right != -1:
                node.right = Node(right)
                node.right.depth = node.depth + 1
                queue.append(node.right)
    
    def swap_node(self, k):
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node.depth % k == 0:
                node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def in_order_traverse(self, node, result):
        if node:
            self.in_order_traverse(node.left, result)
            result.append(node.data)
            self.in_order_traverse(node.right, result)
        return result

            #
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    # # deserialize
    results = []
    # binary_tree = Node(1)
    # queue = deque([binary_tree])
    # for node in indexes:
    #     cur_node = queue.pop()
    #     if node[0] != -1:
    #         cur_node.left = Node(node[0])
    #         queue.append(cur_node.left)
    #     if node[1] != -1:
    #         cur_node.right = Node(node[0])
    #         queue.append(cur_node.right)
    tree = Tree()
    tree.create_tree(indexes)
    for k in queries:
        tree.swap_node(k)
        result = tree.in_order_traverse(tree.root, [])
        results.append(result)
    return results
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
