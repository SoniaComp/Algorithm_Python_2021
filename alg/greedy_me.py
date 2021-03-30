def maxProfit(self, prices: List[int]) -> int:
  result = 0
  for i in range(len(prices)-1):
    if prices[i+1] > prices[i]:
      result += prices[i+1] - prices[i]
  return result

  # return sum(n-p for n, p in zip(prices[1:], pricces) if n > p)