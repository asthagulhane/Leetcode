class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Step 1: Sort to group duplicates and enable pruning
        
        def backtrack(start: int, target: int, path: list[int]):
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Step 2: Skip identical elements at the same level to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Step 3: Early pruning - subsequent elements are too large
                if candidates[i] > target:
                    break
                
                # Choose, Explore, Unchoose
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return res
