import sys

dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 기능 하나 분리
# 브루트포스

def range_check(y, x, r, N, M):
    for i in range(-1, 2, 2):
        ty = y + r*i
        tx = x + r*i
        if ty < 0 or ty >= N or tx < 0 or tx >= M:
            return False
    return True


def solution(N, M, grid):
    ans = 1
    visited = [[0]*M for _ in range(N)]
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] == '.':
                continue
            k = 0
            while 1:
                if range_check(i, j, k, N, M):
                    if grid[i+k][j] == '#' and grid[i-k][j] == '#' and grid[i][j+k] == '#' and grid[i][j-k] == '#':
                        ans *= (1+4*k)

                        for c in range(k):
                            grid[i+c][j], grid[i][j+c], grid[i-c][j], grid[i][j-c] = '#'
                    else:
                        break
                else: break
    return ans


def main():
    stdin = sys.stdin
    N, M = map(int, stdin.readline().split())
    grid = [list(str(stdin.readline().strip())) for _ in range(N)]
    print(solution(N, M, grid))


if __name__ == "__main__":
    main()
