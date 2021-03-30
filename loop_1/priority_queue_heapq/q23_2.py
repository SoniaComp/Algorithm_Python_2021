import heapq
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# heapq 모듈은 이진트리(binary tree)기반의 최소 힙(min heap) 자료구조를 제공합니다.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        root = result = ListNode(None)
        heap = []
        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            # 가장 작은 값 나옴
            node = heapq.heappop(heap)
            # 다음 값으로 연결 오름차순
            result.next = node[2]
            idx = node[1]
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx,  result.next))

        return root.next
