# class Solution:

#     def canTraverseAllPairs(self, nums: list[int]) -> bool:
#         n = len(nums)
#         if n == 1:
#             return True

#         # 1. Build the graph by checking all pairs
#         adj = [[] for _ in range(n)]
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if math.gcd(nums[i], nums[j]) > 1:
#                     adj[i].append(j)
#                     adj[j].append(i)

#         # 2. Check full connectivity using BFS
#         visited = [False] * n
#         queue = [0]
#         visited[0] = True

#         for node in queue:
#             for neighbor in adj[node]:
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     queue.append(neighbor)

#         # Return True if every index was reached
#         return all(visited)




class Solution:

    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False

        # Union-Find Parent arrays
        # max(nums) can be up to 100,000 based on problem constraints
        max_val = max(nums)
        parent = list(range(max_val + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Connect each number to its prime factors
        for num in nums:
            temp = num
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    union(num, d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                union(num, temp)

        # Check if all numbers share the same component root
        root_set = {find(num) for num in nums}
        return len(root_set) == 1

