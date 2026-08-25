class Trie:

    def __init__(self):
        """Initializes the trie object."""
        self.root = {}

    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True  # Key '#' marks the end of a valid word

    def search(self, word: str) -> bool:
        """Returns true if the string word is in the trie, and false otherwise."""
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return '#' in curr

    def startsWith(self, prefix: str) -> bool:
        """Returns true if there is a previously inserted string that has the prefix, and false otherwise."""
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True
