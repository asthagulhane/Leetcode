class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = word  # Store the actual word at the leaf node

        res = []
        rows, cols = len(board), len(board[0])

        # 2. Backtracking DFS
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node[char]

            # Word found: extract it and remove from Trie to prevent duplicates
            if '$' in curr_node:
                res.append(curr_node.pop('$'))

            # Mark the current cell as visited
            board[r][c] = '#'

            # Explore all 4 neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    dfs(nr, nc, curr_node)

            # Backtrack: restore the original character
            board[r][c] = char

            # Optimization (Pruning): Remove empty leaf nodes from Trie
            if not curr_node:
                parent_node.pop(char)

        # 3. Launch DFS from every valid starting cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res
