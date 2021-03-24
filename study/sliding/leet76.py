import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        # 오른쪽 오인터 이동
        for right, char in enumerate(s, 1): # 1 index부터 시작
            missing -= need[char] > 0 # -1 씩 한다. 이부분 특이
            need[char] -= 1
            
            # 필요문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right-left <= end-start:
                    start, end = left, right # 갱신
                # left 이동 다 했으니까 다시 left 이동
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
                