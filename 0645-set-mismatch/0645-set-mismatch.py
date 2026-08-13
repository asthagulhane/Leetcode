# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         counts = {}
#         duplicate = missing = -1
        
#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1
            
#         for i in range(1, len(nums) + 1):
#             if i not in counts:
#                 missing = i
#             elif counts[i] == 2:
#                 duplicate = i
                
#         return [duplicate, missing]
 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        i = 0 
        n = len(nums)

        while i < n :
            correct = nums[i] - 1

            if  nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct] , nums[i]

            else:
                i += 1  

        for i  in range (n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        
        return[]
