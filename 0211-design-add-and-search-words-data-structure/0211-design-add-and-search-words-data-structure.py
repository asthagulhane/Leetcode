class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = True  # Marks the end of a valid word

    def search(self, word: str) -> bool:
        def dfs(index, node) -> bool:
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # Wildcard: check all possible child paths
                    return any(dfs(i + 1, child) for key, child in node.items() if key != '$')
                if char not in node:
                    return False
                node = node[char]
            return '$' in node

        return dfs(0, self.trie)
