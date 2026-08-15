class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
    # Sort the array so consecutive elements sit next to each other
        nums.sort()
    
        longest_streak = 1
        current_streak = 1
    
        for i in range(1, len(nums)):
        # Skip duplicate numbers
            if nums[i] == nums[i-1]:
                continue
            
        # If it's consecutive, grow the current streak
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
            # Streak broke, save the max and reset counter
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
            
        return max(longest_streak, current_streak)
