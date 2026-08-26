class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # If the starting point has an obstacle, no paths are possible
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp array stores the number of paths to each column in the current row
        dp = [0] * n 
        dp[0] = 1  # Base case: 1 way to stand at the start

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0  # Obstacle blocks all paths to this cell
                elif c > 0:
                    dp[c] += dp[c - 1]  # Paths from top (dp[c]) + left (dp[c-1])

        return dp[-1]
