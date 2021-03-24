from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # python counter and 연산
        t_count = Counter(t)
        current_count = Counter()
        
        start = float('-inf')
        end = float('inf')
        
        left = 0
        
        # 오른쪽 포인터로 이동
        for right, char in enumerate(s, 1):
            current_count[char] += 1
            
            # AND 연산 결과로 왼쪽 포인터 이동 판단
            # 모두 존재하는지 체크하는 우아한 코드, 그러나 Counter끼리 AND연산은 오래 걸리는 무거운 연산
            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        return s[start: end] if end - start <= len(s) else ''
                