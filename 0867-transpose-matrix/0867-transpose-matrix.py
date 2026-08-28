class Solution:

    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # Transpose using standard nested loop comprehension swapping row/col indices
        return [
            [matrix[r][c] for r in range(len(matrix))]
            for c in range(len(matrix[0]))
        ]
