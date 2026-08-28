# class Solution:

#     def rotate(self, matrix: list[list[int]]) -> None:
#         """Do not return anything, modify matrix in-place instead."""
#         # 1. Reverse the matrix upside down
#         matrix.reverse()

#         # 2. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
#         for i in range(len(matrix)):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



class Solution:

    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # 1. Create a deep copy helper matrix to store original values
        # Space Complexity: O(n^2)
        original = [row[:] for row in matrix]

        # 2. Map every element from the original to its new position in matrix
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = original[i][j]
