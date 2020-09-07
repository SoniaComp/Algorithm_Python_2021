# 비트 연산
# 그냥 단순히 <<

# 벽에 가기 전에, 존재하는지 여부 체크 잊지 않기

# 인접하는 구역을 어떻게 하는지가 제일 고민됐는데, visited에 구역번호를 해서,
# 다시 루프를 돎.

import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(castle, visited, r, c, zone_num):
    visited[r][c] = zone_num
    queue = [(r, c)]
    cnt = 1
    while queue:
        y, x = queue.pop()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not castle[y][x] & (1 << i) and not visited[ny][nx]:
                visited[ny][nx] = zone_num
                queue.append((ny, nx))
                cnt += 1
    return cnt


def solution_3(visited, space, n, m):
    ans = 0
    for r in range(m):
        for c in range(n):
            for i in (2, 3):
                ny, nx = r+dy[i], c+dx[i]
                if 0 <= ny < m and 0 <= nx < n and visited[r][c] - visited[ny][nx]:
                    temp = space[visited[r][c]] + space[visited[ny][nx]]
                    if temp > ans:
                        ans = temp
    return ans


def solution(castle, n, m):
    check = [[0 for i in range(n)] for j in range(m)]
    count = [0]

    zone_num = 1
    for r in range(m):
        for c in range(n):
            if check[r][c] is 0:
                cnt = bfs(castle, check, r, c, zone_num)
                count.append(cnt)
                zone_num += 1
    print(len(count)-1)
    print(max(count))
    print(solution_3(check, count, n, m))


def main():
    stdin = sys.stdin
    n, m = map(int, stdin.readline().split())
    castle = [list(map(int, stdin.readline().split())) for _ in range(m)]
    solution(castle, n, m)


if __name__ == '__main__':
    main()
