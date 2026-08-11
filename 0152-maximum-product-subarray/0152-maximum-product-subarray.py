# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         max_product = nums[0]
#         n = len(nums) 

#         for left in range(n):
#             current_product = 1 
#             for right  in range (left , n ):
#                 current_product *= nums[right] 

#                 if current_product > max_product :
#                     max_product =current_product
#         return max_product




class Solution:
    def maxProduct(self,nums:List[int]):
        max_ending = nums[0]
        min_ending = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            current_max = max(num,num * max_ending,num * min_ending)
            current_min = min(num,num * max_ending,num * min_ending)
            max_ending = current_max
            min_ending = current_min

            answer = max(answer,max_ending)
        return answer

