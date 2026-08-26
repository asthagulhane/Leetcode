class Solution:

    def maxProduct(self, nums: list[int]) -> int:
        # Initialize trackers with the first element
        res = cur_max = cur_min = nums[0]

        for n in nums[1:]:
            # Negative numbers swap the min and max, so we track both
            vals = (n, n * cur_max, n * cur_min)
            cur_max = max(vals)
            cur_min = min(vals)

            # Update the global maximum product found so far
            res = max(res, cur_max)

        return res
 