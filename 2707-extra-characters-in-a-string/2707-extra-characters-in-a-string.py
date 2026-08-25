from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        words = set(dictionary)
        n = len(s)
        
        @cache
        def dp(i: int) -> int:
            if i == n:
                return 0
            
            # Option 1: Treat current character s[i] as an extra character
            res = 1 + dp(i + 1)
            
            # Option 2: Check all possible substrings starting at index i
            for j in range(i, n):
                if s[i:j+1] in words:
                    res = min(res, dp(j + 1))
                    
            return res
            
        return dp(0)
