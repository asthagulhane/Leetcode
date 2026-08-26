class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_cost = 0
        visited = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0  # Start with the first point
        
        for _ in range(n):
            # Find the unvisited node with the minimum distance
            u = min((d, i) for i, d in enumerate(dist) if not visited[i])[1]
            
            visited[u] = True
            min_cost += dist[u]
            
            # Update distances to remaining unvisited nodes
            x1, y1 = points[u]
            for v in range(n):
                if not visited[v]:
                    d = abs(x1 - points[v][0]) + abs(y1 - points[v][1])
                    if d < dist[v]:
                        dist[v] = d
                        
        return min_cost
