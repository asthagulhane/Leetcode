# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         majority_num = None 
#         count = 0

#         for num in  nums :
#             if count == 0  :
#                 majority_num = num 

#             if  num == majority_num :
#                 count += 1
#             else:
#                 count -= 1
#         return majority_num




# class Solution:
#     def majorityElement(self, nums):

#         freq = {}

#         for num in nums:

#             freq[num] = freq.get(num, 0) + 1

#             if freq[num] > len(nums) // 2:
#                 return num


class Solution:
    def majorityElement(self, nums):

        candidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate