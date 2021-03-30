from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_hash = defaultdict(int)
        start = end = 0
        max_length = 0
        
        while start <= end:
            if end == len(s):
                break
            str_hash[end] += 1
            if str_hash[end]:
                start += 1
                max_length -= 1
            else:
                max_length += 1
            end += 1
                
        return max_length