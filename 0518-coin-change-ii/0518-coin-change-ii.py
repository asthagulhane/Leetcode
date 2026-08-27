class Solution:

    def change(self, amount: int, coins: list[int]) -> int:
        # dp[i] stores the number of ways to make amount i
        dp = [0] * (amount + 1) 
        dp[0] = 1  # Base case: 1 way to make an amount of 0 (using no coins)

        # Loop through each coin type to prevent duplicate combinations
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
