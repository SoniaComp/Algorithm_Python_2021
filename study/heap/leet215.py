import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        # heap = list()
        # for n in nums:
        #     heapq.heappush(heap, -n)
          # heapq 모듈은 최소 힙만 지원하므로 음수로 저장한 다음 가장 낮은 수부터 추출

        # for _ in range(k):
            # heapq.heappop(heap)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        
        # return -heapq.heappop(heap)
        return heapq.heappop(nums)

        # nlargest 이용
        # return heapq.nlargest(k, nums)[-1]

        # 정렬
        # return sorted(nums, reverse=True)[k-1]
