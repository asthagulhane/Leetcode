# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = float('-inf')
#         current_sum = 0

#         for num in  nums:
#             current_sum += num
#             if current_sum > max_sum :
#                 max_sum = current_sum
#             if current_sum < 0 :
#                 current_sum = 0
#         return max_sum 









# class Solution:
#     def maxSubArray(self, nums):

#         current_sum = nums[0]
#         max_sum = nums[0]

#         for num in nums[1:]:

#             current_sum = max(num, current_sum + num)

#             max_sum = max(max_sum, current_sum)

#         return max_sum







class Solution:
    def maxSubArray(self, nums):

        max_sum = float('-inf')
        current_sum = 0

        for num in nums:

            current_sum += num

            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return max_sum

        