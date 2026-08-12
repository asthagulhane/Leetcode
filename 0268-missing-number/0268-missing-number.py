# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:

#         n =len(nums)

#         expected_sum =  (n *(n+1)) // 2

#         actual_sum = sum(nums)

#         return expected_sum - actual_sum








# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)

#         expected_sum = n *(n +  1)// 2 
#         actual_sum = sum(nums)

#         return expected_sum  - actual_sum





class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for  i in range(len(nums)):
            missing ^= i
            missing ^=  nums[i]

        return missing
