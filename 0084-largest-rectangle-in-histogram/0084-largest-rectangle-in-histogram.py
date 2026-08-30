class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # Stores indices
        max_area = 0
        heights.append(0) # Sentinel value to flush the stack at the end
        
        for i, h in enumerate(heights):
            # Maintain a monotonic increasing stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, the bar extends to the very beginning (index 0)
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        return max_area
