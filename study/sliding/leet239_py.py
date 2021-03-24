import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        max_val = max(nums[:k])
        res.append(max_val)
        for i in range(k, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            elif nums[i-k] == max_val:
                max_val = max(nums[i-k+1:i+1])
            res.append(max_val)
        return res