class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
    
        zero_rows = set()
        zero_cols = set()
    
    # Step 1: Scan the matrix to find where the zeros are
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
                
    # Step 2: Update the rows
        for r in zero_rows:
            for c in range(COLS):
                matrix[r][c] = 0
            
    # Step 3: Update the columns
        for c in zero_cols:
            for r in range(ROWS):
                matrix[r][c] = 0




 



        