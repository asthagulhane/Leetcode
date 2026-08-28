class Solution:

    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            # Shift answer left to make room, then add the lowest bit of n
            ans = (ans << 1) | (n & 1)
            n >>= 1  # Shift n right to process the next bit
        return ans
