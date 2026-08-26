class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
            
        # Maximize the number of 3s based on the remainder when divided by 3
        rem = n % 3
        if rem == 0: return 3 ** (n // 3) 
        if rem == 1: return 3 ** (n // 3 - 1) * 4 
        return 3 ** (n // 3) * 2
