from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        
        # Optimization 1: Quick frequency check
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        if any(word_counts[char] > board_counts[char] for char in word_counts):
            return False
        
        # Optimization 2: Start from the rarer end to minimize backtracking branches
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r, c, i):
            if i == len(word): 
                return True
            if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[i]: 
                return False
            
            # Mark visited by temporarily removing the letter
            temp, board[r][c] = board[r][c], '#'
            
            # Explore neighbors
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or 
                     dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            
            # Backtrack
            board[r][c] = temp
            return found

        return any(dfs(r, c, 0) for r in range(R) for c in range(C))
