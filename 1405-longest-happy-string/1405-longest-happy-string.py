class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Keep track of counts and characters in a list
        counts = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = []
        
        while True:
            # Always sort to get the character with the highest count first
            counts.sort(reverse=True)
            
            # Try to pick the character with the most remaining counts
            for i in range(3):
                val, char = counts[i]
                
                # If there are no counts left for this character, we can't build any further
                if val == 0:
                    return "".join(res)
                
                # Check the constraint: avoids building "aaa", "bbb", or "ccc"
                if len(res) >= 2 and res[-1] == res[-2] == char:
                    continue  # Move to the second most frequent character
                
                # Append the valid character, decrement its count, and break to re-sort
                res.append(char)
                counts[i][0] -= 1
                break
            else:
                # If we loop through all characters and none can be validly appended, finish
                return "".join(res)
