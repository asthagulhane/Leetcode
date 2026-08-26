class Solution:

    def buildMatrix(
        self,
        k: int,
        rowConditions: list[list[int]],
        colConditions: list[list[int]],
    ) -> list[list[int]]:
        def topo_sort(conditions):
            adj = [[] for _ in range(k + 1)]
            in_degree = [0] * (k + 1)
            for u, v in conditions:
                adj[u].append(v)
                in_degree[v] += 1

            # Find all nodes with 0 in-degree to start the queue
            queue = [i for i in range(1, k + 1) if in_degree[i] == 0]

            # Standard Kahn's algorithm using list iteration as a queue
            for u in queue:
                for v in adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

            return queue if len(queue) == k else []

        # Get the sorted ordering for rows and columns
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        # If a cycle is detected in either condition, return an empty matrix
        if not row_order or not col_order:
            return []

        # Map each value to its respective row and column index
        row_pos = {val: i for i, val in enumerate(row_order)}
        col_pos = {val: i for i, val in enumerate(col_order)}

        # Construct the final matrix
        matrix = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            matrix[row_pos[x]][col_pos[x]] = x

        return matrix
