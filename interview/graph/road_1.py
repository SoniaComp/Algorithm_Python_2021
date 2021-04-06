def roadsAndLibraries(n, c_lib, c_road, cities):
    cost = 0
    
    if c_lib < c_road:
        return cost*n
    
    success = [True]+[False]*n
    graph = [[0]*(n+1) for _ in range(n+1)]
    
    for fr, to in cities:
        graph[fr][to] = 1
        graph[to][fr] = 1
    
    def dfs(start):
        sub_cost = 0
        if len(set(success)) == 1:
            return 0
        
        for to, connect in enumerate(graph[start][1:]):
            if not success[to+1]:
                success[to+1] = True
                sub_cost += c_road
                sub_cost += dfs(to+1)
        return sub_cost
        
    connected = [(sum(graph[x]), x) for x in range(1, n+1)]
    connected.sort()
    while connected:
        _, x = connected.pop()
        if not success[x]:
            cost += c_lib
            success[x] = True
            cost += dfs(x)
            
    return cost