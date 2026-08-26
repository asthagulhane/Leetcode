class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val 
        
        # Step 2: DFS function to find the product path
        def dfs(src: str, dst: str, visited: set) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    product = dfs(neighbor, dst, visited)
                    if product != -1.0:
                        return weight * product
            return -1.0

        # Step 3: Process queries
        
        return [dfs(q[0], q[1], set()) for q in queries]
