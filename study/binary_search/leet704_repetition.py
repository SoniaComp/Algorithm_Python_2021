# 재귀 풀이가 더 우아한 편이지만, 반복 풀이는 좀 더 직관적이라 이해가 쉽다는 장점이 있다.
# 재귀보다 반복이 더 빠르다.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1
    