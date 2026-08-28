class Solution:

    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b & mask:
            carry = (a & b) << 1
            a = (a ^ b) & mask  # Keep a within 32-bit bounds
            b = carry & mask  # Keep b within 32-bit bounds

        # If a is a positive signed 32-bit int, return it.
        # Otherwise, decode the 32-bit negative value using two's complement.
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
