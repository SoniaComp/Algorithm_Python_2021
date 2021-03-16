# 파이썬은 가급적 모든 재귀풀이가 1000회 반복 이내에 풀이가 가능하도록 구현
# sys.getrecursionlimit() -> 1000

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else: # nums[mid] == target
                    return mid
            else:
                return -1
            
        return binary_search(0, len(nums)-1) # 시작 인덱스와 마지막 인덱스
    