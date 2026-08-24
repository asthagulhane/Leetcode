from functools import reduce
from operator import or_


class Solution:

    def subsetXORSum(self, nums: list[int]) -> int:
        # Bitwise OR of all elements multiplied by 2^(n-1)
            return reduce(or_, nums, 0) << (len(nums) - 1)
