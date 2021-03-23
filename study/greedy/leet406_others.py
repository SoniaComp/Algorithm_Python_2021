import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for pair in sorted(people, key=lambda x: (-x[0], x[1])): # -로 heappush하는 대신 깔끔하게 sorted
            res.insert(pair[1], pair)
        return res