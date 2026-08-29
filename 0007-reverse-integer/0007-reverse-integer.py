class Solution:
    def reverse(self, x: int) -> int:
        # Reverse the absolute value as a string, then restore the sign
        res = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        
        # Check for 32-bit signed integer overflow bounds
        return res if -(2**31) <= res <= 2**31 - 1 else 0
