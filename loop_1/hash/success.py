# q31
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda x: x[0], Counter(nums).most_common(k)))
        # return [ x for x, _ in Counter(nums).most_common(k) ]