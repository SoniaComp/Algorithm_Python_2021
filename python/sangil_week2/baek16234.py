# A[r][c] 명이 살고 있다.
# 1. L 명이상, R 명 이하라면, 할동안 연다.
# 2. 국경선이 인접한 칸 만을 이동할 수 있고, 하루동안 연합
# 3. 연합을 이루고 있는 각 칸의 인구수: 인구수 / 칸의 개수
# 4. 연합을 해체하고, 모든 국경선을 닫는다.

# 이 문제가 좀 더 어려운 점
# 보통 DFS 문제는 한 사이클만 도는데,
# 이 문제의 경우, 새로 인구수를 계산해서, 다시 돌아와서 기록까지 해야함
# 시간복잡도: 2초 - 50*100*2,000*2 = 0.2 초
# 왔다갔다 해도 충분!!

import sys

dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(current, A, union, union_num):
    cx, cy = current
    queue = [(cx, cy)]
    count = 0
    total_num = 0
    while queue:
      x, y = queue.pop()
      union[x][y] = union_num
      count += 1
      total_num += A[x][y]
      for dx, dy in dr:
        if union[x+dx][y+dy] == -1:
          queue.append((x+dx, y+dy))
    new_num = total_num // count
    return A, union, new_num

def solution(N, L, R, A):
    ans = 0
    while 1:
        union = [[-1]*N for _ in range(N)]  # 연합
        union_num = 0  # 연합 그룹 number
        new_nums = []
        for x in range(N):
          for y in range(N):
            if union[x][y] == -1 :
              A, union, new_num = bfs((x, y), A, union, union_num)
              new_nums.apped(new_num)
              union_num += 1
        if union_num == 0: # 인구 이동 없었음
          break
        for x in range(N):
          for y in range(N):
            A[x][y] = new_nums[union[x][y]]
        ans += 1
    return ans


def main():
    stdin = sys.stdin
    N, L, R = map(int, stdin.readline().split())
    A = [map(int, stdin.readline().split()) for _ in range(N)]
    solution(L, R, A)


if __name__ == "__main__":
    main()
