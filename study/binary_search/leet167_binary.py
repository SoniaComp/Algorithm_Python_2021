def twoSum(self, numbers: List[int], target:int) -> List[int]:
  for k, v in enumerate(numbers):
    left, right = k + 1, len(numbers) -1
    # 이진 검색으로 나머지 값 판별
    expected = target - v # 나머지 값
    while left <= right:
      mid = left + (right - left) // 2
      if numbers[mid] < expected:
        left = mid + 1
      elif numbers[mid] > expected:
        right = mid -1
      else:
        return k+1, mid+1
        