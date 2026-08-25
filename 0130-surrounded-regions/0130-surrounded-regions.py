class Solution:
    def solve(self, board: list[list[str]]) -> None:
        R, C = len(board), len(board[0])
        
        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':
                board[r][c] = '#'  # Mark as safe (connected to border)
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    dfs(nr, nc)

        # 1. Start DFS from all border 'O's to mark unsubmerged regions
        borders = [(r, c) for r in range(R) for c in (0, C - 1)] + \
                [(r, c) for c in range(C) for r in (0, R - 1)]
                  
        for r, c in borders:
            dfs(r, c)

        # 2. Flip surrounded 'O' to 'X', and restore '#' back to 'O'
        for r in range(R):
            for c in range(C):
                board[r][c] = 'O' if board[r][c] == '#' else 'X'
