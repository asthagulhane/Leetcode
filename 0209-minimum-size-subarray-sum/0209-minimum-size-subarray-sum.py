# class Solution :
#     def minSubArrayLen(self,target : int,nums:List[int]):
#         n = len(nums)
#         min_length = float('inf')

#         # check every possible starting position
#         for i in range(n):
#             current_sum = 0
#             # Expand the subarray from the starting position 
#             for  j in range(i , n):
#                 current_sum += nums[j]

#                 # As soon as the condition is met,record length and break 
#                 if current_sum >=  target :
#                     min_length = min(min_length , j - i + 1)
#                     break 

#         return min_length if min_length != float('inf') else 0









class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0 
        min_length = float('inf')

        # expand the window using the right pointer
        for right in range (len(nums)):
            current_sum += nums[right]

            # shrink the window from the left as the condition is met 
            while current_sum >= target:
                min_length = min(min_length,right -left + 1 )
                current_sum -= nums[left]
                left += 1
        return min_length if min_length!= float('inf') else 0 

 