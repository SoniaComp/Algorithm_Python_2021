from collections import defaultdict, Counter

# 갖고 있는 돌 S의 개수를 각각 모두 헤아린 다음, J의 각 요소를 키로 하는 각 개수를 합산하면 풀이할 수 있다.
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
      # freqs = defaultdict(int)
      count = 0

      # # 비교 없이 돌(S) 빈도수 계산
      # for char in S:
      #   freqs[char] += 1
      freqs = Counter(S) # 돌(S) 빈도 수 계산

      for char in J:
        count += freqs[char]

      return count
      
      # counter를 사용하면 코드를 더욱 짧게 줄일 수 있다.
      # https://excelsior-cjh.tistory.com/94

      # 이거를 한줄로 줄일수도 있다.
      # return sum(s in J for s in S) # TRUE의 개수를 리턴한다.


