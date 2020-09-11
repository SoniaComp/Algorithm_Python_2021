import sys
MAX = sys.maxsize


def solution(miro):
    dp = [MAX] * (len(miro)+100)  # 최소 점프 횟수
    dp[0] = 0
    for i in range(len(miro)-1):
        for j in range(1, miro[i]+1):
            dp[i+j] = min(dp[i+j], dp[i]+1)
    if dp[len(miro)-1] == MAX:
      return -1
    return dp[len(miro)-1]


def main():
    stdin = sys.stdin
    N = map(int, input())
    miro = list(map(int, stdin.readline().split()))
    print(solution(miro))


if __name__ == "__main__":
    main()
