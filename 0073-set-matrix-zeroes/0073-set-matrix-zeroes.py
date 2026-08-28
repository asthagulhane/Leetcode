class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False  # Track if the first row needs to be zeroed

        # 1. Determine which rows and columns need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark the column header
                    if r > 0:
                        matrix[r][0] = 0  # Mark the row header
                    else:
                        row_zero = True

        # 2. Use the headers to zero out cells (excluding first row/col for now)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 3. Handle the first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 4. Handle the first row if needed
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
   