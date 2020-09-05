# 파이썬 공부할 때 참고하면 좋은 사이트!
# 프로그래머스: 파이썬을 파이썬 답게
# https://programmers.co.kr/learn/courses/4008/lessons/12732

import sys


def solution(N, M, miro):  # bfs
    for i in range(1, N+1):
        for j in range(1, M+1):
            miro[i][j] += max(miro[i][j-1], miro[i-1][j], miro[i-1][j-1])
    return miro[-1][-1]


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    miro = [[0]*(M+1)] + [[0]+list(map(int, stdin.readline().split())) for _ in range(N)]
    print(solution(N, M, miro))


if __name__ == '__main__':
    main()

# PADDING을 넣어준다.

## 파이썬으로 BFS 구현 방법
'''
from collectios import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        queue += graph[n] - set(visited)
    
    return visited
'''

## 파이썬으로 DFS 구현 방법
'''
def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    
    return visited
'''