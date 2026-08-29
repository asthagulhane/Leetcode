class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        remaining = n - 1
        pos = 1
        
        # Embed the bits of (n - 1) into the 0-bit positions of x
        while remaining > 0:
            if not (x & pos):
                if remaining & 1:
                    ans |= pos
                remaining >>= 1
            pos <<= 1
            
        return ans
