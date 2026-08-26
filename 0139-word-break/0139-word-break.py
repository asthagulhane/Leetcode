class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        max_len = max(len(w) for w in words) if words else 0
        dp = [True] + [False] * len(s)
        
        for i in range(1, len(s) + 1):
            # Only check substrings up to the maximum word length to stay highly optimized
            dp[i] = any(dp[j] and s[j:i] in words for j in range(max(0, i - max_len), i))
            
        return dp[-1]
