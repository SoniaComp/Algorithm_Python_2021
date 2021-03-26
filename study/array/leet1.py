class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 풀이 1 '''
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        
        ''' 풀이 2 '''
#         for i, n in enumerate(nums):
#             complement = target - n
            
#             if complement in nums[i+1:]:
#                 return nums.index(n), nums[i+1:].index(complement) + (i+1)
        
        ''' 풀이 3 : 해시 '''
#         nums_maps = {}
#         # 키와 값을 바꿔 딕셔너리로 저장
#         for i, num in enumerate(nums):
#             nums_map[num] = i
        
#         # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i= nums_map[target-num]:
#                 return nums.index(num), nums_map[target_num]

        ''' 풀이 4 : 투 포인터 '''
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 크면 오른족 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right