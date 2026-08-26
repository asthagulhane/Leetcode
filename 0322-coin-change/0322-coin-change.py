class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize DP table with a value greater than any possible solution
        dp = [0] + [amount + 1] * amount
        
        # Compute the minimum coins for each sub-amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] <= amount else -1
