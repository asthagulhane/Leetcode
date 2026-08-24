import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Group projects by (capital, profit) and sort them by required capital
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        max_heap = []
        i, n = 0, len(projects)
        
        # Maximize capital up to k times
        for _ in range(k):
            # Push profits of all projects we can currently afford into the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # Negative for max-heap simulation
                i += 1
            
            # If no projects are affordable, we cannot proceed further
            if not max_heap:
                break
            
            # Pop the most profitable project and add its profit to current capital
            w -= heapq.heappop(max_heap)
            
        return w
