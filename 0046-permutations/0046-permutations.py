from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start: int):
            if start == len(nums):
                res.append(nums[:])  # Append a copy of the current arrangement
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)                         # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (Undo swap)
                
        backtrack(0)
        return res
