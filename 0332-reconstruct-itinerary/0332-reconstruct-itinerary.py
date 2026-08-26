class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Build adjacency list with reverse sorted destinations for O(1) popping
        graph = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []
        stack = ["JFK"]

        # Hierholzer's Algorithm (DFS)
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())

        # Reverse the itinerary to get the correct chronological order
        return itinerary[::-1]
