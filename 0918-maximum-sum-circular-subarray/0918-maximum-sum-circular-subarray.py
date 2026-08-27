class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        max_sum = current_max = float('-inf')
        min_sum = current_min = float('inf')
        
        for x in nums:
            total_sum += x
            
            # Standard Kadane's for maximum subarray
            current_max = max(x, current_max + x)
            max_sum = max(max_sum, current_max)
            
            # Modified Kadane's for minimum subarray
            current_min = min(x, current_min + x)
            min_sum = min(min_sum, current_min)
            
        # If all elements are negative, total_sum == min_sum.
        # In that case, return max_sum directly.
        return max_sum if max_sum < 0 else max(max_sum, total_sum - min_sum)
