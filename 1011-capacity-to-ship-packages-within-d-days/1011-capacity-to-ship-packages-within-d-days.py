class Solution:

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            current_days = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    current_days += 1
                    current_weight = w
                    if current_days > days:
                        return False
                else:
                    current_weight += w
            return True

        # Lower bound: max item weight (must fit on the ship)
        # Upper bound: sum of all weights (ship everything in 1 day)
        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid  # Try to find a smaller valid capacity
            else:
                low = mid + 1  # Capacity is too small, increase it

        return low
