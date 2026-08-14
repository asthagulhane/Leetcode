# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_count = 0
#         n = len(nums)
        
#         # Check sequences starting at each position
#         for i in range(n):
#             current_count = 0
#             for j in range(i, n):
#                 if nums[j] == 1:
#                     current_count += 1
#                 else:
#                     break  # Stop when a 0 is encountered
            
#                 max_count = max(max_count, current_count)
                    
#         return max_count




class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        streak = 0
        
        for val in nums:
            if val == 1:
                streak += 1
                if streak > ans:
                    ans = streak
            else:
                streak = 0 # Broken streak, reset to zero
                
        return ans






        