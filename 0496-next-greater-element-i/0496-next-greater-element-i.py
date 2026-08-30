class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}
        
        # Precompute next greater elements for nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        # Map values to answers, defaulting to -1 if no greater element exists
        return [next_greater.get(num, -1) for num in nums1]
