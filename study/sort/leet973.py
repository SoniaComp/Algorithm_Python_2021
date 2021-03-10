import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result

# 우선순위 큐는 주로 힙으로 구현한다.
# 파이썬의 heapq모듈은 최소 힙(Min Heap)이기 때문에, 거리가 가까운 순을 출력해야 하는 이 문제 풀이에 더욱 적합하다.