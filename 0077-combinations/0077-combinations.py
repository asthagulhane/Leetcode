class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, path: list[int]):
            # Base case: if the combination is complete
            if len(path) == k:
                result.append(list(path))
                return
            
            # Pruning optimization: Only loop if there are enough remaining 
            # elements left to choose from to make a valid combination of size k
            upper_bound = n - (k - len(path)) + 2
            for i in range(start, upper_bound):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # Backtrack
                
        backtrack(1, [])
        return result
