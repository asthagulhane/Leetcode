class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            # Adjust to 0-indexed for proper modulo 26 arithmetic
            columnNumber -= 1

            # Get the remainder (0 for 'A', 25 for 'Z')
            remainder = columnNumber % 26

            # Convert remainder to character and store
            res.append(chr(65 + remainder))

            # Reduce columnNumber for the next position
            columnNumber //= 26 

        # The characters were gathered right-to-left, so reverse the result
        return "".join(reversed(res))
