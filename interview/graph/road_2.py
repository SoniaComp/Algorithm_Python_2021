def dfs(nodes, node, visited):
    if visited[node]:
      return 0
    visited[node] = 1
    count = 1
    for neighbor in nodes[node]:
      count += dfs(nodes, neighbor, visited)
    return count
    
def roadsAndLibraries(n, c_lib, c_road, cities):
    cost = 0 
    if c_lib < c_road:
        return c_lib * n
 
    nodes = {i+1: [] for i in range(n)}
    visited = [0] * (n+1)
    for u, v in cities:
      nodes[u].append(v)
      nodes[v].append(u)
    
    for node in nodes:
      count = dfs(nodes, node, visited)
      if count:
        cost += c_lib + (count-1)*min(c_lib, c_road)

    return cost