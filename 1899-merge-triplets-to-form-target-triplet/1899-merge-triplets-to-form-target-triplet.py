class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # Track whether we can match each of the 3 target values
        found = [False, False, False]
        x, y, z = target
        
        for a, b, c in triplets:
            # Skip triplets that exceed any target dimension
            if a > x or b > y or c > z:
                continue
                
            # If a value matches the target, mark its position as found
            if a == x: found[0] = True
            if b == y: found[1] = True
            if c == z: found[2] = True
            
            # Early exit if all target elements can be formed
            if all(found):
                return True
                
        return False
