class Solution:

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Priority queue stores (distance, node)
        pq = [(0, k)]
        dist = {}

        # Dijkstra's algorithm
        while pq:
            d, node = heapq.heappop(pq)
            if node not in dist:
                dist[node] = d
                for neighbor, weight in graph[node]:
                    if neighbor not in dist:
                        heapq.heappush(pq, (d + weight, neighbor))

        # Check if all nodes are reached
        return max(dist.values()) if len(dist) == n else -1
