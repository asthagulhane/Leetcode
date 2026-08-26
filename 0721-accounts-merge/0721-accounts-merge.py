class Solution:

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Map each email to its owner's name and build an adjacency list
        email_to_name = {}
        graph = defaultdict(list)

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name

        # Traverse the graph to find connected components
        visited = set()
        merged_accounts = []

        for email in graph:
            if email not in visited:
                # Iterative DFS
                stack = [email]
                visited.add(email)
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                # Sort the emails and prepend the name
                name = email_to_name[email]
                merged_accounts.append([name] + sorted(component))

        return merged_accounts
