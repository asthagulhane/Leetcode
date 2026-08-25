from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)  # O(1) lookups
        
        @cache
        def dfs(i: int) -> list[str]:
            if i == len(s): 
                return [""]
            
            return [
                s[i:j] + (" " + suf if suf else "")
                for j in range(i + 1, len(s) + 1)
                if s[i:j] in words
                for suf in dfs(j)
            ]
            
        return dfs(0)
