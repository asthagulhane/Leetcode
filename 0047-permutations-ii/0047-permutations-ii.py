from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        counts = Counter(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in counts:
                if counts[num] > 0:
                    counts[num] -= 1
                    backtrack(path + [num])
                    counts[num] += 1  # Backtrack
                    
        backtrack([])
        return res
