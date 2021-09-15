from collections import defaultdict
class SolutionFirst:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
          graph[a].append(b)
        # 한번 방문한 노드는 더 이상 탐색하지 않는 형태, 가지 치기로 최적화한 문제 풀이
        visited = [False] * numCourses
        locked = set()

        def dfs(i):
          if visited[i]:
            return True
          
          if i in locked: # 순환
            return False
          
          locked.add(i)
          for p in graph[i]:
            if not dfs(p):
              return False
          locked.remove(i)
          visited[i] = True
          return True

        for i in range(numCourses):
          if not dfs(i):
            return False
        
        return True

Solution = SolutionFirst
      
        