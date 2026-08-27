class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad boundaries with 1
        A = [1] + nums + [1]
        
        @cache
        def dp(i, j):
            if i + 1 >= j:
                return 0
            # Choose the last balloon k to burst in the interval (i, j)
            return max(A[i] * A[k] * A[j] + dp(i, k) + dp(k, j) for k in range(i + 1, j))
            
        return dp(0, len(A) - 1)
