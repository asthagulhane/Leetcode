class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = unmatched_close = 0
        
        for char in s:
            if char == '(':
                unmatched_open += 1
            elif unmatched_open:
                unmatched_open -= 1
            else:
                unmatched_close += 1
                
        return unmatched_open + unmatched_close
