class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0: 
            return False
        
        target = total_sum // 2
        bits = 1
        
        for num in nums:
            bits |= bits << num
            
        return bool((bits >> target) & 1)
