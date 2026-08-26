class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text2 is the shorter string to optimize space
        if len(text1) < len(text2):
            text1, text2 = text2, text1
            
        dp = [0] * (len(text2) + 1)
        
        for c1 in text1:
            cur = [0] * (len(text2) + 1)
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    cur[j + 1] = dp[j] + 1
                else:
                    cur[j + 1] = max(dp[j + 1], cur[j])
            dp = cur
            
        return dp[-1]
