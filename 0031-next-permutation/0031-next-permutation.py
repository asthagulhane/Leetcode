from typing import List  

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find pivot
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        # Step 2: Find next greater element
        if pivot >= 0:
            j = n - 1
            while nums[j] <= nums[pivot]:
                j -= 1

            nums[pivot], nums[j] = nums[j], nums[pivot]

        # Step 3: Reverse suffix
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1