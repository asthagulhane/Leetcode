class Solution:

    def findOrder(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        # Build graph representation and count in-degrees
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        # Queue all courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        # Process courses via BFS (Kahn's algorithm)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Return the valid order, or an empty list if a cycle prevents completion
        return order if len(order) == numCourses else []
