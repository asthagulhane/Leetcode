class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= left <= right:
            # If the lightest and heaviest person can fit together
            if people[left] + people[right] <= limit:
                left += 1  # Lightest person gets on the boat
                
            # The heaviest person always gets a boat (either alone or paired)
            right -= 1
            boats += 1  # Increment boat count
            
        return boats

        