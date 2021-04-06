from collections import defaultdict, deque

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
  maps = defaultdict(list) # {from:to}
  color = [0] + ids # color dict도 만드는 게  {node:color}

  # 연결관계 만들기
  for i in range(len(graph_from)):
    maps[graph_from[i]].append(graph_to[i])
    maps[graph_to[i]].append(graph_from[i])
    
  # 시작점이 val...?
  q = deque([(val, 0)])
  start_color = color[val]
  print(start_color)
  visited = set()

  while q:
    current, cnt = q.popleft()
    visited.add(current)

    for x in maps[current]:
      if x not in visited:
        if color[x] == start_color:
          return cnt + 1
        visited.add(x)
        q.append((x, cnt+1))

  return -1
