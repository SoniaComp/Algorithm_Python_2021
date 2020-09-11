import sys


def solution(N, room):
    dp = [[[0]*3 for _ in range(16)]for _ in range(16)]
    dp[0][1][0] = 1
    for j in range(2, N):
        if not room[0][j]:
            if not room[0][j]:
                dp[0][j][0] = dp[0][j-1][0]
    for i in range(1, N):
        for j in range(2, N):
            if not room[i][j] and not room[i][j-1] and not room[i-1][j]:
                dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            if not room[i][j]:
                dp[i][j][0] = dp[i][j-1][0]+dp[i][j-1][1]
                dp[i][j][2] = dp[i-1][j][1]+dp[i-1][j][2]
    return sum(dp[N-1][N-1])

def main():
    stdin = sys.stdin
    N = int(input())
    home = [list(map(int, stdin.readline().split()))
                          for _ in range(N)]
    print(solution(N, home))


if __name__ == "__main__":
    main()
