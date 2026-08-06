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
# from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n + 1)

        for num in nums:
            freq[num] += 1

            duplicate = -1
            missing = -1

        for num in range(1, n + 1):
            if freq[num] == 2:
                duplicate = num
            elif freq[num] == 0:
                missing = num

        return [duplicate, missing]
