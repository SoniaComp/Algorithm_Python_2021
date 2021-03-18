# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = [ ]
        
        # 각 연결리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

# heapq 모듈 사용법: https://www.daleseo.com/python-heapq/
# 이진 트리 기반의 최소 힙 자료구조
# min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은값은 언제나 인덱스 0, 즉, 이진 트리의 루트에 위치합니다. 내부적으로 min heap 내의 모든 원소(k)는 항상 자식 원소들(2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제됩니다.
        
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
            
        return root.next