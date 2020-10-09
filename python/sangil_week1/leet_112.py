class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                benefit+= prices[i+1]-prices[i]
        return benefit

# 상길북
def maxProfit(self, prices: List[int]) -> int:
    # 0보다 크면 무조건 합산.. 파이썬 다운 방식
    return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices-1)))