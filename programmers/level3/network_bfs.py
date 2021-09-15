def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    def bfs(n, computers, com, visited):
        visited[com] = True
        queue = []
        queue.append(com)
        while len(queue) != 0:
            com = queue.pop(0)
            visited[com] = True
            for connect in range(n):
                if connect != com and computers[com][connect] == 1:
                    if visited[connect] == False:
                        queue.append(connect)
                        
    for com in range(n):
        if visited[com] == False:
            bfs(n, computers, com, visited)
            answer += 1
    return answer