# 나도 백준이와 같은 마음

# 예제가 많을 때는 예제를 많이 해본다. 귀납적인 거신가...?

# 브루트 포스!?!?!? -> 범위가 너무 크다.
# DP: 처음부터 쭉 하면서, 번 최대 금액 체크
import sys


def solution(N, T, P):
    dp = [0]*(N+1)
    for i in range(N):
        # if works[i][0] <= N-i:  # 더 일 안하고! 딱 정해진 날짜에 퇴사!
        #     dp[i+works[i][0]] = max(dp[i+works[i][0]], dp[i]+works[i][1])

        # dp[i+1] = max(dp[i+1], dp[i])
        if i + T[i] < N+1:
            dp[i+T[i]] = max(dp[i]+P[i], dp[i+T[i]])
        dp[i+1] = max(dp[i+1], dp[i])
    return dp[N]


def main():
    stdin = sys.stdin
    N = int(input())  # [T,P]
    # works = [list(map(int, input().split())) for _ in range(N)]
    T, P = [], []
    for i in range(N):
        tmp = [int(i) for i in sys.stdin.readline().split()]
        T.append(tmp[0])
        P.append(tmp[1])
    print(solution(N, T, P))


if __name__ == "__main__":
    main()
