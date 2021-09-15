from collections import defaultdict

class SolutionFirst:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
      INF = float('inf')
      igraph = [[] for _ in range(n)]
      for fr, to, price in flights:
        igraph[to].append((fr, price))
      cache = {}

      def _find(num_flight, city):
        if num_flight < 0:
          return INF
        elif city == src:
          return 0

        key = (num_flight, city)

        if  key not in cache:
          cache[key] = min((_find(num_flight-1, pre_city)+price for pre_city, price in igraph[city]), default=INF)
        return cache[key]

      cache = {}
      cheapest = _find(K+1, dst)
      return cheapest if cheapest!=INF else -1

from heapq import heappush, heappop

class SolutionSecond:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INF = float('inf')
        graph = [[]for _ in range(n)]
        for fr, to, price in flights:
          graph[fr].append((to, price))
        
        dists = defaultdict(lambda:INF)
        heap = [(0, 0, src)]
        while heap:
          price, count, fr = heappop(heap)
          if fr == dst and count <= K+1:
            return price

          
          key = (count, fr)
          if price >= dists[key] or count > K+1:
            dists[key] = price
            for to, p in graph[fr]:
              heappush(heap, (price+p, count+1,to))
              
          return -1