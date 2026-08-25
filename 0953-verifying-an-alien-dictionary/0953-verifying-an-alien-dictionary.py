class Solution:

    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Map each character to its index/rank for O(1) lookups
        rank = {char: i for i, char in enumerate(order)}

        # Convert a word into a list of its character ranks
        def get_ranks(word):
            return [rank[char] for char in word]

        # Check if every adjacent pair of words is correctly ordered
        return all(
            get_ranks(w1) <= get_ranks(w2) for w1, w2 in zip(words, words[1:])
        )
