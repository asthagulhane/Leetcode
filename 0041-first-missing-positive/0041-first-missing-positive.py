# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         target = 1
        
#         # Check every integer starting from 1
#         while True:
#             # If the current target is not in the array, it's the missing one
#             if target not in nums:
#                 return target
#             target += 1








class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)


        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Scan the array to find the first index out of place
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are correct, the missing number is n + 1
        return n + 1
