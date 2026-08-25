class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_len = sum(matchsticks)
        
        # A square must have 4 equal integer sides
        if total_len % 4 != 0:
            return False
        
        target = total_len // 4
        # Sort in descending order so larger sticks fail early if they don't fit
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4 
        
        def dfs(index: int) -> bool:
            # Base case: All matchsticks successfully assigned
            if index == len(matchsticks):
                return True
            
            for i in range(4):
                # Check if the matchstick fits on the current side
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index] # Backtrack
                
                # Pruning: If a side is 0, subsequent empty sides are identical; 
                # trying them will only lead to redundant duplicate states.
                if sides[i] == 0:
                    break
                    
            return False
            
        return dfs(0)
 