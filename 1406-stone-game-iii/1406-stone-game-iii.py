class Solution:

    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp tracking the relative score advantages for the next 3 positions
        dp = [0, 0, 0]

        for i in range(n - 1, -1, -1):            
            res = float("-inf")
            take = 0 
            # A player can take 1, 2, or 3 stones
            for k in range(min(3, n - i)):
                take += stoneValue[i + k]
                res = max(res, take - dp[k])
            # Slide the window to include the current optimal relative score
            dp = [res] + dp[:2]

        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
