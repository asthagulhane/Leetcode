# class Solution:
#     def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
#         # Build adjacency list
#         adj = {i: [] for i in range(n)}
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)
            
#         # DFS helper to find the max height (edges) from a node
#         def get_height(node, parent):
#             children_heights = [get_height(nei, node) for nei in adj[node] if nei != parent]
#             return 1 + max(children_heights + [-1])

#         # Calculate height for all possible roots
#         heights = [get_height(i, -1) for i in range(n)]
#         min_h = min(heights)
        
#         # Return all roots that achieve the minimum height
#         return [i for i, h in enumerate(heights) if h == min_h]






from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # Edge case: 1 or 2 nodes are already the answer
        if n <= 2:
            return list(range(n))
        
        # Build adjacency list and track node degrees
        adj = {i: set() for i in range(n)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        # Initialize queue with all initial leaves (degree == 1)
        leaves = deque([i for i in adj if len(adj[i]) == 1])
        
        # Keep trimming leaves until 1 or 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # Remove the leaf from its only neighbor's connection
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                # If neighbor becomes a leaf, add it to the queue
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
                    
        # The remaining nodes are the centroids/roots of MHTs
        return list(leaves)

