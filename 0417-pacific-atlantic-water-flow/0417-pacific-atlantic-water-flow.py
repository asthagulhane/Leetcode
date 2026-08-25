class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            queue = list(starts)  # Use a simple list as a queue for speed
            for r, c in queue:
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if (0 <= nr < m and 0 <= nc < n and 
                        (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        # Ocean boundary coordinates
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
        
        # Intersection of cells that can reach both oceans
        return [list(cell) for cell in bfs(pacific_starts) & bfs(atlantic_starts)]
