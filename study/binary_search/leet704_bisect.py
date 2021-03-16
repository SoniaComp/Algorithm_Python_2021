# 파이썬에는 이진 검색 알고리즘을 지원하는 bisect 모듈을 기본으로 제공한다.
# 여러가지 예외처리를 포함한 이진 검색 알고리즘이 깔끔하게 모듈 형태로 구현되어 있다.
import bisect

def search(self, nums: List[int], target: int) -> int:
  index = bisect.bisect_left

  if index < len(nums) and nums[index] == target:
    return index

  else:
    return -1
