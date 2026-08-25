class Solution:

    @cache
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[]]

        return [
            [s[:i]] + rest
            for i in range(1, len(s) + 1)
            if s[:i] == s[:i][::-1]  # Check if prefix is a palindrome
            for rest in self.partition(s[i:])  # Recursively partition the remaining suffix
        ]
