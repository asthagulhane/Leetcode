class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1: return True  # Cycle detected
            if state[v] == 2: return False # Already verified safe
            
            state[v] = 1 # Mark as visiting
            if any(has_cycle(neighbor) for neighbor in graph[v]):
                return True
                
            state[v] = 2 # Mark as fully processed
            return False

        # Check every course for a cycle
        return not any(has_cycle(i) for i in range(numCourses) if state[i] == 0)
