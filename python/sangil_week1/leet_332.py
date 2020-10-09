class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        linked = {}
        # for ticket in tickets:
        #     linked[ticket[0]] = ticket[1]
        # 여러개가 있을 경우, 사전 순으로...
        for ticket in tickets:
            try:
                if linked[ticket[0]] and linked[ticket[1]] > ticket[1]:
                    linked[ticket[0]] = ticket[1]
            except:
                linked[ticket[0]] = ticket[1]
        result = ['JFK']
        current = 'JFK'
        for i in range(len(tickets)):
            result.append(linked [current])
            current = linked[current]
        return result
        
## 상길북
############################
# 풀이1. DFS로 일정 그래프 구성
import collections

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
  # 그래프 구성 작업
  graph = collections.defaultdict(list)
  # 그래프 순서대로 구성
  for a, b in sorted(tickets):
    graph[a].append(b)
  
  route = []
  def dfs(a):
    # 첫번째 값을 읽어 어휘순 방문
    while graph[a]:
      dfs(graph[a].pop(0))
    route.append(a)

  dfs('JFK')
  # 다시 뒤집어 어휘 순 결과로
  return route[::-1]

############################
# 풀이 2
# pop(0)과 pop()의 차이
# pop의 시간 복잡도를 O(n) 에서 O(1) 로 개선
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
  graph = collections.defaultdict(list)
  # 그래프 반대 순서
  for a, b in sorted(tickets, reverse = True):
    graph[a].append(b)
  
  route = []
  def dfs(a):
    # pop() 으로 시간 복잡도 줄임
    while graph[a]:
      dfs(graph[a].pop())
    route.append(a)

  dfs('JFK')
  return route[::-1]

############################
# 풀이 3
# 대부분의 재귀 문제는 반복으로 치환할 수 있으며, 스택으로 풀이가 가능하다. 
# dfs 가 아니기 때문에
# 한번 방문했던 곳을 다시 방문하지 않으려면,
# 별도로 마킹하여 다음번에 방문하지 않거나 아예 스택의 pop()으로 값을 제거하는 방법이 있다.
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
  graph = collections.defaultdict(list)
  for a, b in sorted(tickets):
    graph[a].append(b)
  
  route, stack = [], ['JFK']
  while stack:
    # 스택으로 반복되는 부분 pop으로 처리
    #### 이 부분이 신기했음
    while graph[stack[-1]]:
      stack.append(graph[stack[-1]].pop(0))
  return route[::-1]