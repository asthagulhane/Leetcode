class Solution:

    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Expected sum minus actual sum gives the missing number
        return (n * (n + 1)) // 2 - sum(nums)
