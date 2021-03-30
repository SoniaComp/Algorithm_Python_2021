# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not len(lists):
            return []
        if len(lists) == 1:
            return lists[0]
        
        head = lists[0]
        for idx in range(1, len(lists)):
            new = lists[idx]
            node = head
            while new.next:
                while node.next and new.next:
                    if node.val > new.val:
                        new.next, node.next, new = node.next, new, new.next
                    else:
                        new, node = new.next, node.next
        return head