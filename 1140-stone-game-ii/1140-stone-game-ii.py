class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        # suffix_sums[i] represents the total stones remaining from index i to the end
        suffix_sums = list(accumulate(piles[::-1]))[::-1]
        
        @cache
        def dfs(i, m):
            # If a player can take all the remaining piles, they will do so
            if i + 2 * m >= n:
                return suffix_sums[i]
            
            # Maximize current player's stones by minimizing opponent's yield
            return suffix_sums[i] - min(dfs(i + x, max(m, x)) for x in range(1, 2 * m + 1))
            
        return dfs(0, 1)
