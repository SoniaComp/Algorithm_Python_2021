def search(self, nums: List[int], target: int) -> int:
  try:
    return nums.index(target)
  except:
    return -1

# index 메소드 사용 -> 값이 존재하지 않으면 에러가 발생하므로 예외처리를 할 수 있다.

# index와 이진검색
# 앞에서 부터 차례대로 찾는 index()함수는 최악의 경우 O(n)으로, 뒤에 위치한 값잀록 점점 찾는 속도가 느려지며, 이처럼 1000배나 가까이 차이가 나는 경우도 생길 수 있다.
# 반면 이진검색은 항상 일정한 속도를 보인다. O(logn)으로, 아무리 큰 값이라도 속도 차이가 거의 없다. 로그의 효과 떄문이다. 

# C에서는 오버플로우가 발생한다.

# 자료형을 초과하지 않는 이진검색 코드
# mid = left + (right - left) // 2