class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] stores the number of combinations that add up to i
        dp = [0] * (target + 1) 
        dp[0] = 1  # Base case: 1 way to make a target of 0 (empty combination)

        # Build up solutions for all sub-targets
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]
