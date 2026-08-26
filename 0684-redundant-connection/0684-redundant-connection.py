class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # n edges means n nodes in this specific graph structure
        parent = list(range(len(edges) + 1))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])  # Path compression
            return parent[i]
            
        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return [u, v]  # Found the cycle-causing edge
            parent[root_u] = root_v
