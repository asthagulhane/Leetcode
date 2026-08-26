class Solution:
    def numSquares(self, n: int) -> int:
        # Check if n is a perfect square
        if int(math.isqrt(n))**2 == n:
            return 1
        
        # Check Legendre's theorem: n = 4^a * (8b + 7) returns 4
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        
        # Check if it can be decomposed into 2 squares
        for i in range(1, math.isqrt(n) + 1):
            if int(math.isqrt(n - i*i))**2 == n - i*i:
                return 2
                
        # If not 1, 2, or 4, it must be 3
        return 3
