import itertools


class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Generate the Cartesian product of the letter groups
        pools = (mapping[digit] for digit in digits)
        return ["".join(comb) for comb in itertools.product(*pools)]
