class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res, stack = [-1] * n, []
        
        # Iterate through a virtually doubled array
        for i in range(n * 2):
            idx = i % n
            # Clear elements from the stack smaller than the current element
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]
            stack.append(idx)
            
        return res
