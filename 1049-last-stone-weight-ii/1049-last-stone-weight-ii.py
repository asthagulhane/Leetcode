class Solution:

    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        target = total // 2 

        # Tracks all possible subset sums <= target
        dp = {0}
        for stone in stones:
            dp |= {x + stone for x in dp if x + stone <= target}

        return total - 2 * max(dp)
