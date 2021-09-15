from collections import deque
    
def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    
    def bfs(v, visited, ad):
        count = 0
        q = deque([[v, count]])
        while q:
            value = q.popleft()
            v, count = value
            if visited[v] == -1:
                visited[v] = count
                count += 1
                for e in adj[v]:
                    q.append([e, count])
                    
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer