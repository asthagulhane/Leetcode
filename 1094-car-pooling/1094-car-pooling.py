class Solution:

    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Step 1: Initialize a difference array for coordinates 0 to 1000
        passenger_changes = [0] * 1001

        # Step 2: Record passenger changes at pick-up and drop-off points
        for num_passengers, start, end in trips:
            passenger_changes[start] += num_passengers
            passenger_changes[end] -= num_passengers

        # Step 3: Track current passengers and check against capacity
        current_passengers = 0
        for change in passenger_changes:
            current_passengers += change
            if current_passengers > capacity:
                return False

        return True
