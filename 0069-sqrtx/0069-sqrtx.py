class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        # Increment i until its square exceeds x
        while i * i <= x:
            i += 1
        # The previous integer is the correct truncated square root
        return i - 1
