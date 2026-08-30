from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # If the next element is larger, a peak must exist to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, a peak exists on the left side (or is mid itself)
            else:
                right = mid
                
        return left
