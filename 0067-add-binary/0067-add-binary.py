class Solution:

    def addBinary(self, a: str, b: str) -> str:
        # int(x, 2) converts binary string to integer
        # bin() converts it back to '0b...' so we slice from index 2 onwards
        return bin(int(a, 2) + int(b, 2))[2:]
