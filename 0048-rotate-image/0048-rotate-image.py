class Solution:

    def rotate(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        # 1. Reverse the matrix upside down
        matrix.reverse()

        # 2. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
