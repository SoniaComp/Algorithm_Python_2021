from typing import List
from heapq import heappush, heappop, heapify

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# hack. to avoid comparision of ListNode, insert index to element in front of ListNode.
class SolutionFirst:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # list comprehension으로 for 문 대체
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(heap)

        root = ListNode(0)
        cur = root # 너무 한꺼번에 쓰는 것도 좋지 않다.
        
        while heap:
          _, i, node = heappop(heap) # 파이썬
          cur.next = node
          if node.next:
            node = node.next
            heappush(heap, (node.val, i, node))
            
          cur.next = None
          return root.next