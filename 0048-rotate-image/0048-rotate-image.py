class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # 1. transpose row into column 
        for r in  range (n):
            for c in  range (r + 1 , n ):
                # swap the element across diagonal
                matrix[r][c], matrix[c][r] =  matrix[c][r], matrix[r][c]

        # reverse the row
        for r in range (n):
             matrix[r].reverse()
