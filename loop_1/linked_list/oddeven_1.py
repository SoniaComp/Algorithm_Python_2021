# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_nodes = []
        even_nodes = []
        cur = head
        index = 1
        while cur:
            if index % 2 == 1:
                odd_nodes.append(cur)
            else:
                even_nodes.append(cur)
            index += 1
            cur = cur.next
        root = ListNode()
        cur = root
        for node in odd_nodes:
            cur.next = node
            cur = node
        for node in even_nodes:
            cur.next = node
            cur = node
        cur.next = None
        return root.next