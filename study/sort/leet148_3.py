# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# 분할 / 정복 / 병합
class Solution:        
    def sortList(self, head: ListNode) -> ListNode:
        # 연결리스트 -> 파이썬 리스트
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
        
        # 정렬
        lst.sort()
        
        # 파이썬 리스트 -> 연결리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
            
        return head

# 콤마연산자
'''
merged += i, # 콤마는 중첨 리스트로 만들어주는 역할을 한다.
merged += [i] 와 같음
'''