# class Solution:
#     def containsDuplicate(self, nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i] == nums[j]:
#                     return True
#         return False




class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for  num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



     