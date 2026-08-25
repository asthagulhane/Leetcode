class Solution:

    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(r, c):
            # Check boundaries and if the cell is land ('1')
            if (
                0 <= r < len(grid)
                and 0 <= c < len(grid[0])
                and grid[r][c] == "1"
            ):
                grid[r][c] = "0"  # Sink the land to mark it visited
                dfs(r + 1, c)  # Down
                dfs(r - 1, c)  # Up
                dfs(r, c + 1)  # Right
                dfs(r, c - 1)  # Left

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)  # Visit the entire island
                    count += 1  # Increment island count

        return count
