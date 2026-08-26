class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # Append original index to each edge before sorting
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])
        
        # Helper to compute MST weight with options to skip or force an edge
        def get_mst(skip_idx=-1, force_idx=-1):
            parent = list(range(n))
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
            
            weight, count = 0, 0
            
            # Force inclusion of an edge if specified
            if force_idx != -1:
                for u, v, w, idx in edges:
                    if idx == force_idx:
                        parent[find(u)] = find(v)
                        weight += w
                        count += 1
                        break
            
            # Standard Kruskal's algorithm
            for u, v, w, idx in edges:
                if idx == skip_idx:
                    continue
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    parent[root_u] = root_v
                    weight += w
                    count += 1
                    if count == n - 1:
                        break
            
            return weight if count == n - 1 else float('inf')

        # Find base MST weight
        base_weight = get_mst()
        critical, pseudo = [], []
        
        # Evaluate each edge's classification
        for u, v, w, idx in edges:
            # If removing it increases weight or disconnects graph, it's critical
            if get_mst(skip_idx=idx) > base_weight:
                critical.append(idx)
            # If forcing it still yields the optimal MST weight, it's pseudo-critical
            elif get_mst(force_idx=idx) == base_weight:
                pseudo.append(idx)
                
        return [critical, pseudo]
