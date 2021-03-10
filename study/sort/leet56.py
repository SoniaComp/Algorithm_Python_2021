class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        # 먼저 첫번째값으로 sorting
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]: # 들어간 값의 최대값과 비교
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged
                