# 가장 이해가 잘 됐던 설명
# https://rhdtka21.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-BOJ-17070-17069-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-2
# 방의 각각의 칸을 표현하기 위해서 총 3차원 리스트를 사용해서 풀 수 있다.

# dp를 이용해서 풀어보자
import sys
# 가로, # 세로, # 전체 - 대각선
check = [(0, 1), (1, 0), (1, 1)]
state = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]

def solution(N, home):
    m = N+1
    dp = [[0]*m for _ in range(m)]
    queue = [(1, 2, 0)]
    while len(queue):
        x, y, st = queue.pop()
        check_slash = 1
        for i in range(len(check)):
            ny, nx = x+check[i][0], y+check[i][1]
            if ny > N:
                continue
            if nx > N:
                continue
            if i == 2 and check_slash == 0:
                break
            if home[ny][nx]:
                check_slash = 0
            if home[ny][nx] == 0:
                if state[st][i]:
                    queue.append((nx, ny, i))
                    dp[nx][ny] += 1
    return dp[N][N]


def main():
    stdin = sys.stdin
    N = int(input())
    home = [[0]*(N+1)] + [[0]+list(map(int, stdin.readline().split()))
                          for _ in range(N)]
    print(solution(N, home))


if __name__ == "__main__":
    main()
