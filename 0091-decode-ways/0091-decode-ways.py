class Solution:
    
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # prev1 represents dp[i-1], prev2 represents dp[i-2]
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            current = 0

            # Check if single-digit decoding is valid
            if s[i] != "0":
                current += prev1

            # Check if two-digit decoding is valid
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                current += prev2

            # If no valid decodings are possible, break early
            if current == 0:
                return 0

            prev2, prev1 = prev1, current

        return prev1
