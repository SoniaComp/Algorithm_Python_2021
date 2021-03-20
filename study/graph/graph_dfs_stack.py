def iterative_dfs(start_v):
  discovored = []
  stack = [start_v]
  while stack:
    v = stack.pop()
    if v not in discovored:
      discovored.apped(v)
      for w in graph[v]:
        stack.append(w)
  return discovored