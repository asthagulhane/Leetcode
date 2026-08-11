# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         result = []

#         for i in range(len(nums)):
#             current_sum = 0 

#             for  j in range (i + 1):
#                 current_sum += nums[j]

#             result.append(current_sum)

#         return result  




# class Solution :
#     def runningSum(self , nums):
#         result = []
#         current_sum = 0
#         for num in nums:
#             current_sum += num
#             result.append(current_sum)
#         return result




class Solution :
    def runningSum(self , nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums