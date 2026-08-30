class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            # Group consecutive identical characters and count them
            s = "".join(f"{len(list(group))}{key}" for key, group in groupby(s))
        return s
