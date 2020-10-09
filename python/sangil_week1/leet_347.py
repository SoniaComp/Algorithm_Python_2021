'''
대표적인 정렬문제.. 
NlogN 으로 풀어야 한다!!

복잡도: 빅오 표기법(최악의 경우)
'''

# 첫번째 그냥 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        frequent = {}
        num = nums[0]
        count = 0
        for n in nums:
            if num == n:
                count += 1
            else:
                frequent[num] = count
                count = 1
                num = n
            if n == nums[len(num) - 1]:
                frequent[num] = count
        frequent_num = sorted(frequent)  # 오답
        # frequent_num = [v for i, v in sorted(frequent.items(), key=lambda item: item[1])]
        return frequent_num[:k]


# 상길북 참조
'''
* PriorityQueue를 이용은 스레드 세이프를 보장 -> 오히려 락킹 오버헤드의 가능성도 있다.
* heapq 모듈은 스레드세이프를 보장하지 않아서, 1번 스레드의 값이 2번 스레드에서 변경될 수 있다.
* 하지만 파이썬은 멀티 스레딩이 거의 의미가 없고, 대부분 멀티 프로세싱으로 활용한다.
실무에서 우선순위 큐는 대부분 heapq로 구현하고 있으며, 우선순위 큐를 사용하는 문제 풀이 또한 heapq를 사용해 풀이한다.
'''

# 첫번째 방법
import collections
import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    for f in freqs:
      heapq.heappush(freqs_heap, (-freqs[f], f))
      # 힙은 키 순서대로 정렬되기 때문에, 빈도 수를 키로 한 것
    topk = list()
    # k 번만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
      topk.append(heapq.heappop(freqs_heap[1]))
    return topk

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
    # most_common: 빈도수가 높은 순서대로 아이템을 추출하는 기능을 제공한다.
    # zip -> python 3+ 부터 generator를 리턴한다.
    # 제너레이터: 루프의 반복 동작을 제어할 수 있는 루틴 형태
    # * 언패킹
