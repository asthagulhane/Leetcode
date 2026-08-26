class Solution:

    def longestPalindrome(self, s: str) -> str:
        # Check all possible lengths, starting from the longest
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                sub = s[start : start + length]

                # Check if the substring is a palindrome
                if sub == sub[::-1]:
                    return sub
        return ""
