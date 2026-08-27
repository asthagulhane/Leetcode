class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        memo = {}
        
        def dp(i, j):
            if i > j: 
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Maximize Alice's score relative to Bob's score
            memo[(i, j)] = max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))
            return memo[(i, j)]
            
        return dp(0, len(piles) - 1) > 0 
