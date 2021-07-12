class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
                return
            
            grid[i][j] = 0
            
            # 동서 남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

from collections import deque
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0]) # 이런식으로 의미없는 컬럼 값 줄이고, 정수화

        def bfs(sr, sc):
            queue = deque()
            queue.append((sr, sc))
            grid[sr][sc] = '#'
            while queue:
                pr, pc = queue.popleft()
                for dr, dc in directions:
                    r, c = pr+dr, pc + dc
                    if not (0<=r<R and 0<=c<C) or grid[r][c] != '1':
                        continue
                    grid[r][c] = '#'
                    queue.append((r, c))

        # 예외 처리
        if not grid:
            return 0
        count = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == '1':
                    bfs(row, col)
                    count += 1

        return count