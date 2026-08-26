class Solution:

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev2, prev1 = 0, 0
        for c in cost:
            prev2, prev1 = prev1, c + min(prev2, prev1)
        return min(prev2, prev1)
