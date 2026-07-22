class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        n = len(nums) 

        for left in range(n):
            current_product = 1 
            for right  in range (left , n ):
                current_product *= nums[right] 

                if current_product > max_product :
                    max_product =current_product
        return max_product
