import sys

dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(N, M, grid):
    ans = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#':
                end_flag = False
                count = 0
                while 1:
                    for x, y in dr:
                        x *= count+1
                        y *= count+1
                        if grid[i+x][j+y] == '#' and visited[i+x][j+y] == 0:
                            end_flag = True
                            break
                    if end_flag:
                        if count:
                            for cnt in range(count+1):
                                for x, y in dr:
                                    x *= cnt+1
                                    y *= cnt+1
                                    visited[i+x][j+y] = 1
                        break
                    else:
                        count += 1
                if count:
                    ans *= 1+4*count
    return ans

def main():
    stdin = sys.stdin
    N, M = map(int, stdin.readline().split())
    grid = [list(str(stdin.readline().strip())) for _ in range(N)]
    solution(N, M, grid)


if __name__ == "__main__":
    main()
