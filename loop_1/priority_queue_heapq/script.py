from typing import List
from heapq import heappush, heappop, heapify

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# hack. to avoid comparision of ListNode, insert index to element in front of ListNode.
# 88ms, 17.5MB (99%, 82%)
class SolutionFirst:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(heap)
        root = ListNode(0)
        cur = root
        while heap:
            _, i, node = heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heappush(heap, (node.val, i, node))
        cur.next = None
        return root.next


Solution = SolutionFirst