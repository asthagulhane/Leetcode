class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Track minimum cost to reach each city
        prices = [float('inf')] * n
        prices[src] = 0
        
        # Relax edges k + 1 times (k stops = max k + 1 flights)
        for _ in range(k + 1):
            temp_prices = list(prices)
            for u, v, w in flights:
                if prices[u] != float('inf') and prices[u] + w < temp_prices[v]:
                    temp_prices[v] = prices[u] + w
            prices = temp_prices
            
        return prices[dst] if prices[dst] != float('inf') else -1
