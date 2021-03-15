import heapq
from collections import Counter

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
  freqs = Counter(nums)
  freqs_heap = []
  # 힙에 음수로 삽입
  for f in freqs:
    heapq.heappush(freqs_heap, (-freqs[f], f))
  
  topk = list()
  # k번만큼 추출, 최소힙(Min Heap)이므로 가장 작은 음수순으로 추출

  for _ in range(k): # _이렇게 쓰일 경우에는 이게 값으로 쓰이지는 않는다.
    topk.append(heapq.heappop(freqs_heap)[1])

  return topk

  