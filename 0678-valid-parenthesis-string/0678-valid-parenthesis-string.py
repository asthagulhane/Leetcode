class Solution:

    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0  # Range of possible open parentheses count

        for char in s:
            cmin += 1 if char == "(" else -1
            cmax += 1 if char != ")" else -1

            if cmax < 0:
                return False  # Too many ')' even if all '*' were '('

            cmin = max(cmin, 0)  # cmin can't be negative (can't have negative open brackets)

        return cmin == 0
