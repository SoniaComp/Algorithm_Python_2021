# 슬라이싱
# 파이썬 슬라이싱은 매번 새롭게 객체를 생성해서 할당하는 과정을 거침으로, 엄청나게 큰 배열의 경우 슬라이싱으로 새로운 객체를 생성하는데 상당한 시간이 든다. 배열의 길이를 계산하는 데도 매번 길이를 계산하는 비용이 들기 때문에, 여기에 상당한 시간이 소요된다. 슬라이싱은 매번 새롭게 배열의 길이를 계산해야 한다.

import bisect 

def twoSum(self, numbers:List[int], target:int) -> List[int]:
  for k, v in enumerate(numbers):
    expected = target - v
    # 1번 방법
    # i = bisect.bisect_left(numbers[k+1:], expected)
    # if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
    # 2번 방법
    # nums = numbers[k+1:]
    # i = bisect.bisect_left(nums, expected)
    # if i < len(nums) and numbers[i+k+1] == expected:
    # 3번 방법
    i = bisect.bisect_left(numbers, expected, k+1)
    if i<len(numbers) and numbers[i] == expected:
      return k+1, i+k+2
