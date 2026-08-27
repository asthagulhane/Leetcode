class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Edge cases: target is out of bounds or combination is mathematically impossible
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        subset_target = (total_sum + target) // 2 
        
        # 1D DP array representing ways to reach each sum
        dp = [1] + [0] * subset_target         
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]
