class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row, cols, diag1, diag2):
            if row == n:
                return 1
            
            count = 0
            # Get a bitmask of all valid positions for the current row
            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
            
            while available:
                # Extract the lowest set bit (next available position)
                position = available & -available
                # Clear this position from available spots
                available ^= position
                
                # Move to the next row, shifting diagonal conflicts accordingly
                count += dfs(row + 1, cols | position, (diag1 | position) << 1, (diag2 | position) >> 1)
                
            return count

        return dfs(0, 0, 0, 0)
