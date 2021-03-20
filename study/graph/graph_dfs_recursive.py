def recursive_dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if not w in discovered:
      discovered = recursive_dfs(w, discovered)
  return discovered
