""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
from collections import deque

def check_in_order(root, prev):
    # if root.left is not None:
    #     check_in_order(root.left, prev)
    # if prev[0] >= root.data:
    #     return False
    # prev[0] = root.data
    # if root.right is not None:
    #     check_in_order(root.right, prev)
    # return True
    result = True
    if root.left is not None:
        result &= check_in_order(root.left, prev)
    if prev[0] >= root.data:
        return False
    prev[0] = root.data
    if root.right is not None:
        result &= check_in_order(root.right, prev)
    return result
    # result &= 연산으로 결과를 합산해줘야한다.

def checkBST(root):
    return check_in_order(root,[-1])
    # queue = deque([root])
    # prev_node = root
    # while queue:
    #     cur_node = queue.pop()
    #     # if (cur_node.left and cur_node.left.data < cur_node.data) and (cur_node.right and cur_node.data < cur_node.right.data and cur_node.right.data < prev_node.data):
    #     #     queue.append(cur_node.left)
    #     #     queue.append(cur_node.right)
    #     #     continue
    #     if cur_node.left 
    #     else:
    #         return False
    # return True
    # 처음에 Queue로 했다가, left의 right data 같은 경우는 root의 데이터 보다 작아야하는데, 그게 안돼서 Pass

    