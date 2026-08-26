class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # State tracking: held (has stock), sold (just sold), reset (cooldown/no stock)
        held, sold, reset = float('-inf'), 0, 0
        
        for p in prices:
            prev_held = held
            held = max(held, reset - p)
            reset = max(reset, sold)
            sold = prev_held + p
            
        return max(sold, reset)
