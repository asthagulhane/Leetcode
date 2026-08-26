class Solution:

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(sub_nums):
            prev2, prev1 = 0, 0
            for num in sub_nums:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        # Compare robbing without the last house vs without the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
