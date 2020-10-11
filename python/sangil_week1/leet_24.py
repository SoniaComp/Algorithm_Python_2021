# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        # 처음에는 result = []에 append하는 식으로 했는데 직접 조작
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

# 상길북 풀이 2
# 반복구조
def swapPairs(self, head: ListNode) -> ListNode:
  root = prev = ListNode(None)
  prev.next = head
  while head and head.next:
    # 뒤에 값 넣기
    b = head.next # b = 2 head = 1
    # 다음값 미리 지정
    head.next = b.next  # head.next = 3
    # 다음값을 1로 바꾸어 놓기
    b.next = head # 2.next = 1

    prev.next = b # 이전 값은 2

    # 다음 두 비교를 위해서...
    head = head.next
    prev = prev.next.next

  return root.next

# 상길북 풀이 2
# 재귀 구조
def swapPairs(self, head: ListNode) -> ListNode:
  if head and head.next:
    p = head.next
    # 스왑된 값 리턴 받음
    head.next = self.swapPairs(p.next)
    p.next = head
    return p
  return head
  # 다른 연결 리스트 문제들의 풀이와 마찬가지로, 실제로는 백트래킹 되면서 연결 리스트가 이어지게 된다.

  # swapPairs(1) -> swapPairs(3) 
  #     2  1          4   3