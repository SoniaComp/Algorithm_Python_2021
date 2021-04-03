from bisect import bisect, bisect_left
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        half = target // 2
        half_idx = bisect(nums, target)
        for i, num in enumerate(nums[:half_idx]):
            new_target = target - num
            idx = bisect_left(nums, new_target, i+1)
            if idx < len(nums) and nums[idx] == new_target:
                return [i+1, idx+1]
        