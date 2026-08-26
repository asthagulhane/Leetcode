class Solution:

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
        queries: list[list[int]],
    ) -> list[bool]:
        # Step 1: Initialize the reachability matrix
        is_prereq = [[False] * numCourses for _ in range(numCourses)]

        # Step 2: Fill in direct dependencies
        for u, v in prerequisites:
            is_prereq[u][v] = True

        # Step 3: Compute indirect reachability (Floyd-Warshall)
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prereq[i][k] and is_prereq[k][j]:
                        is_prereq[i][j] = True

        # Step 4: Answer each query in O(1) constant time
        return [is_prereq[u][v] for u, v in queries]
