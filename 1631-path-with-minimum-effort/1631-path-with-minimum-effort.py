import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        dist = [[float('inf')] * C for _ in range(R)]
        dist[0][0] = 0
        min_heap = [(0, 0, 0)]  # (effort, r, c)
        
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            
            if r == R - 1 and c == C - 1:
                return effort
                
            if effort > dist[r][c]:
                continue
                
            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
        return 0
