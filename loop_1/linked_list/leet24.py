# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ''' 단순히 값만 바꿈 '''
        # cur = head
        # while cur and cur.next:
        #     cur.val, cur.next.val = cur.next.val, cur.val
        #     cur = cur.next.next
        # return head
        ''' 노드 자체를 바꿈(반복 -> 바틈업)'''
#         root = prev = ListNode(None)
#         prev.next = head
#         while head and head.next:
#             # b가 a(head)를 가리키도록 할당
#             b = head.next
#             head.next = b.next
#             b.next = head
            
#             # prev가 b를 가리키도록 할당
#             prev.next = b
            
#             # 다음번 비교를 위해 이동
#             head = head.next
#             prev = prev.next.next
        
#         return root.next
        ''' 노드 자체를 바꿈(재귀) '''
        if head and head.next:
            p = head.next
            # 스왑된 값을 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head