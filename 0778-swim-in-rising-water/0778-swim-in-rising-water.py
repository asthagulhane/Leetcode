import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Min-heap stores: (max_elevation_seen, row, col)
        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        while pq:
            time, r, c = heapq.heappop(pq)
            
            # Reached destination (bottom-right corner)
            if r == n - 1 and c == n - 1:
                return time
                
            # Explore 4-directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Path cost is governed by the maximum elevation encountered
                    heapq.heappush(pq, (max(time, grid[nr][nc]), nr, nc))
