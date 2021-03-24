''' 방법1 : 재귀
class Solution:
    def fib(self, n: int) -> int:
    # 방법1 : 재귀
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
'''
import collections

class Solution:
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        '''메모이제이션
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
        '''
        '''타뷸레이션
        self.dp[1] = 1
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]
        '''
        # 공간 절약
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+ y
        return x
            