class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Maps each number to its last seen index
        last_seen = {}
        
        for i, num in enumerate(nums):
            # Check if we saw this number before and if it's within distance k
            if num in last_seen and i - last_seen[num] <= k:
                return True
            # Update the latest index for this number
            last_seen[num] = i
            
        return False
        