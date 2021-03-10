# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# 분할 / 정복 / 병합
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2,  l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
        
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        # Runner의 기법을 활용한다. 연결리스트는 전체 길이를 알 수 없기 때문에
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None # 분할
        
        # 분할 재귀
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeTwoLists(l1, l2)