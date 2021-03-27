# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
#         q: Deque = collections.deque()
        
#         if not head:
#             return True
        
#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next
            
#         while len(q) > 1:
#             if q.popleft()!=q.pop():
#                 return False
            
#         return True
        # 런너를 이용해 역순 연결 리스트 구성
        rev = None
        slow = fast = None
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # 0 <- 1 <- 2 <- 3
            ''' 
            만약에 
            rev, rev.next = slow, rev # rev, slow 동일한 값 참조 : slow도 1 <- 2 가 되어서, slow.next가 1이 된다.
            slow = slow.next
            
            '''
        if fast: # 홀수개인 경우
            # 0 1 2 3 4 5 6
            # f   f   f   f
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev