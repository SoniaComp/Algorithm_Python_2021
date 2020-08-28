import sys
from collections import deque

dist = []
room = []
trash = []
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
C = 0
R = 0

def solution(C, R):
    answer = sys.maxsize
    for i in range(R):
        c = list(input().strip())
        room.append(c)
        for j, k in enumerate(c):
            if k == 'o':
                sx, sy = i, j
            elif k == '*':
                trash.append([i, j])

    for i in range(R):
        for j in range(C):
            room[i][j] = map(int, input())
            if room[i][j] == '*':
                trash.append([i, j])
            if room[i][j] == 'o':
                start = [i, j]
    dist=[[0]*len(trash)]*len(trash)
    for i in range(len(trash)):
        x, y = trash[i]
        visited = bfs(x, y)
        for j in range(len(trash)):
            if i==j:
                continue
            x, y = trash[j]
            if visited[x][j]==0:
                print(-1)
                return
            else:
                dist[i][j] = visited[x][y]
    print(dist)
            

def bfs(x, y):
    q=deque()
    visited = [[0]*C for _ in range(R)]
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < C and 0 <= ny < R:
                if room[nx][ny] != '*' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    q.append([nx, ny])
    return visited
                    
            
            



while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break
    else:
        solution(C, R)




# NP 완전문제
# NP-완전 문제 중 하나라도 P에 속한다는 것을 증명한다면 모든 NP 문제가 P에 속하기 때문에, P-NP 문제가 P=NP의 형태로 풀리게 된다. 반대로 NP-완전 문제 중의 하나가 P에 속하지 않는다는 것이 증명된다면 P=NP에 대한 반례가 되어 P-NP 문제는 P≠NP의 형태로 풀리게 된다.

# C++ Next Permutation 순열 구하기
# https://twpower.github.io/82-next_permutation-and-prev_permutation