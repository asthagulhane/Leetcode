class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        
        def backtrack(remain, combo, start):
            if remain == 0:
                res.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break  # Pruning
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i) # Reuse same element
                combo.pop()
                
        backtrack(target, [], 0)
        return res
