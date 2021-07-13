from collections import deque

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

class Solution:
  def numIslands(self, grid:List[List[str]]) -> int:
    def bfs(sr, sc, label):
      queue = deque()
      queue.append((sr, sc))
      labels[sr][sc] = label
      while queue:
        pr, pc = queue.popleft()
        for dr, dc in directions:
          r, c = pr + dr, pc + dc
