class Solution:

    def orangesRotting(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # Track coordinates of fresh and rotten oranges
        fresh = {(r, c) for r in range(R) for c in range(C) if grid[r][c] == 1}
        rotten = {(r, c) for r in range(R) for c in range(C) if grid[r][c] == 2}
        minutes = 0

        # Expand rotten oranges layer by layer (BFS)
        while fresh and rotten:
            rotten = {
                (r + dr, c + dc)
                for r, c in rotten
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            } & fresh
            fresh -= rotten
            minutes += 1

        return -1 if fresh else minutes
