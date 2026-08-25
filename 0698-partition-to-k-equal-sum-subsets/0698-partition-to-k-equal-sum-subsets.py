class Solution:

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        nums.sort(reverse=True)  # Optimize: process larger numbers first
        if nums[0] > target:
            return False

        subsets = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    subsets[j] -= nums[i]

                    if (
                        subsets[j] == 0
                    ):  # Optimize: skip identical empty buckets
                        break
            return False

        return backtrack(0)
