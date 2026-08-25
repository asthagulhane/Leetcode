class Solution:

    def cloneGraph(self, node: "Node") -> "Node":
        old_to_new = {}

        def dfs(curr):
            if not curr:
                    return None
            if curr in old_to_new:
                return old_to_new[curr]

            # Create clone and cache it before visiting neighbors to handle cycles
            copy = Node(curr.val)
            old_to_new[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
 