class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: out of bounds or water (0)
            if not (0 <= r < R and 0 <= c < C and grid[r][c] == 1):
                return 0
            
            # Mark cell as visited by sinking it (turning 1 to 0)
            grid[r][c] = 0
            
            # Sum up current cell + 4 neighboring directions
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
        # Check every cell and return the maximum area found
        return max(dfs(r, c) for r in range(R) for c in range(C))
