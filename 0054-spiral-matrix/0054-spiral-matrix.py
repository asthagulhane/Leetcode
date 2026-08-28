class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
        
        # Initialize boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # 1. Traverse top row from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Traverse right column from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # Check if boundaries have crossed
            if not (left < right and top < bottom):
                break
                
            # 3. Traverse bottom row from right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # 4. Traverse left column from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
