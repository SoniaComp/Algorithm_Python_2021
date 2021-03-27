# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # def reverse(node: ListNode, prev: ListNode = None):
        #     if not node:
        #         return prev
        #     next, node.next = node.next, prev
        #     return reverse(next, node)
        # return reverse(head)
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
    
    # 0 1 2
    # 1
    # node, prev = head, None
    # next = 1
    # node.next = None
    # prev = head [Node]
    # node = 1
    # 2
    # next = 2
    # node.next = head
    # prev = 1
    # node = 2
    # 3
    # n