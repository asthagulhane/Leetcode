class Solution:

    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x 
            n = -n

        result = 1
        while n > 0:
            # If current bit is set, multiply result by x
            if n % 2 == 1:
                result *= x
            x *= x  # Square the base
            n //= 2  # Divide exponent by 2

        return result
