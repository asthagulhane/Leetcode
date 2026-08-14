# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         max_profit = 0
#         n = len(prices)
        
#         # Check every pair of days
#         for i in range(n):
#             for j in range(i + 1, n):
#                 profit = prices[j] - prices[i]
#                 if profit > max_profit:
#                     max_profit = profit
                    
#                 return max_profit
        




class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices: 
            if price < min_price:
                min_price = price
           
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
