from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 start 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1 # 이미 등장한 문자 다음으로 가야 한다.
            else:
                max_length = max(max_length, index-start+1)
            used[char] = index # 현재 문자의 위치 삽입
        return max_length

class SolutionRefer:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = defaultdict(lambda: -1)
        max_length = length = 0
        start = 0
        for index, char in enumerate(s):
            if start <= used[char]:
                max_length = max(max_length, length)
                length -= used[char] + 1 - start
                start = used[char] + 1
            length += 1
            used[char] = index
        max_length = max(max_length, length)
        return max_length