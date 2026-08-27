class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        reachable_count = 0
        
        for i in range(1, n):
            # Add new index entering the valid jumping window
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
                
            # Remove old index leaving the valid jumping window
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1
                
            # Current index is reachable if window has valid points and character is '0'
            if reachable_count > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[n - 1]
