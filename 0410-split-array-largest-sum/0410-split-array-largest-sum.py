class Solution:

    def splitArray(self, nums: list[int], k: int) -> int:
        # Helper function to check if a maximum subarray sum of 'mid' is feasible
        def canSplit(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num  # Start a new subarray
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        # Define the search space
        low, high = max(nums), sum(nums)

        # Binary search for the minimized largest sum
        while low < high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid  # Try to find a smaller valid maximum sum
            else:
                low = mid + 1  # Increase the allowed maximum sum

        return low
