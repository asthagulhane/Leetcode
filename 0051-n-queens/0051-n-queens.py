class Solution:

    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        def dfs(queens, diag_diff, diag_sum):
            row = len(queens)
            if row == n:
                # Convert column indices to the required board format
                result.append(
                    ["." * col + "Q" + "." * (n - col - 1) for col in queens]
                )
                return

            for col in range(n):
                # Check column and both diagonal conflicts
                if (
                    col not in queens
                    and (row - col) not in diag_diff
                    and (row + col) not in diag_sum
                ):
                    dfs(
                        queens + [col],
                        diag_diff | {row - col},
                        diag_sum | {row + col},
                    )

        dfs([], set(), set())
        return result
