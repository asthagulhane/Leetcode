from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            # Base case: if pattern is exhausted, string must be exhausted too
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Handle the '*' wildcard logic
            if j + 1 < len(p) and p[j + 1] == '*':
                # Case 1: Skip '*' and its preceding element
                # Case 2: Use '*' if characters match, and advance string index
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
                
            # Normal character match transition
            return match and dfs(i + 1, j + 1)
            
        return dfs(0, 0)
