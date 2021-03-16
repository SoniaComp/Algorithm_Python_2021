import bisect

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
  result: Set = set()
  # 한쪽은 순서대로 탐색하고, 다른 쪽은 정렬해서 이진 검색으로 값을 찾으면, 검색 효율을 획기적으로 높일 수 있다. 
  # sort() nlogn 복잡도

  nums2.sort()
  for n1 in nums1:
    # 이진 검색으로 일치 여부 판별
    i2 = bisect.bisect_left(nums2, n1)
    if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
      result.add(n1)
  return result
 


    # bisect_left(arr, x, lo=0, hi=len(arr))
    # list a에서 값 x가 들어갈 인덱스를 구한다. 리스트의 특정 범위내에서만 이진 탐색을 수행하려고 할 때 사용한다.
    # bisect_right(arr, x)
    # 같은 값이 있으면 그 값의 오른쪽 위치를 취한다.
    # insort(arr, x) bisect로 구해진 위치에 x 값을 삽입한다.
    # insort_left(arr, x) bisect_left()로 구해진 위치에 x값을 삽입한다.

    # 주어진 리스트 a와 값 x가 있을 때, x가 위치해야 할 인덱스를 구하는 함수
    # 그리고 같은 조건에 값 x를 올바를 위치에 삽입하는 함수