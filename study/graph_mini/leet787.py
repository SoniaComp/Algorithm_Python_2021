from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        # 그래프 인접 리스트 구성ㅇ
        for u, v, w in flights:
            graph[u].append((v, w))
            
        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, src, K)]
        
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            # if k <= K:
            #     k += 1
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        
        return -1
                
