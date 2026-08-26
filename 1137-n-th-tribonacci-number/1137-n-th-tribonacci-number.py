class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Initialize the first three Tribonacci numbers
        t0, t1, t2 = 0, 1, 1
        
        # Iteratively update variables to use O(1) extra space
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
            
        return t2
