'''
다익스트라 알고리즘 
다이나믹 프로그래밍을 이용한 최단 경로 찾기 알고리즘이다.
특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알려준다. 
'''
import heapq


def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distance[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

        return distance