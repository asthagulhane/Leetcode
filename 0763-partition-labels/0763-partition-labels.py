class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Precompute the last occurrence index of each character
        last_seen = {char: i for i, char in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            # Expand the boundary of the current partition if needed
            end = max(end, last_seen[char])
            
            # If we reach the maximum index needed for the current partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1  # Reset start for the next partition
                
        return result
