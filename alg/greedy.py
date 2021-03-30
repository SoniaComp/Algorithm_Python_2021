# 문제: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
def maxProfit(self, prices: List[int]) -> int:
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result
     # 두번째 풀이
     # return sum(n - p for p, n in zip(prices, prices[1:]) if n > p)
     # 두번째 방법으로 풀면 좋은 점
     # 1. 파이썬의 언어 스타일에 따라, 인덱스 접근을 지양
     # 2. 뭐든 할 수 있는 코드(ex)인덱스를 포함한 코드)가 아니라, 코드 스타일로 기능을 제한하여 더 보기 쉽고 명확하게 했다.