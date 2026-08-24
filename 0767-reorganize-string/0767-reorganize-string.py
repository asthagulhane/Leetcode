# import itertools

# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         # Generate all unique permutations of the string characters
#         # Using a set ensures we only check unique arrangements
#         unique_permutations = set(itertools.permutations(s))
        
#         for perm in unique_permutations:
#             valid = True
            
#             # Check if any adjacent characters are the same
#             for i in range(len(perm) - 1):
#                 if perm[i] == perm[i + 1]:
#                     valid = False
#                     break
            
#             # Return the first valid rearranged string found
#             if valid:
#                 return "".join(perm)
                
#         return ""



from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        char_counts = Counter(s)
        
        # Step 2: Push all counts to a max-heap (invert count to make it a max-heap in Python)
        max_heap = [[-count, char] for char, count in char_counts.items()]
        heapq.heapify(max_heap)
        
        # Guard clause: If the most frequent character exceeds the valid limit
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
            
        result = []
        prev_count, prev_char = 0, ""
        
        # Step 3: Greedily place the most frequent remaining characters
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            
            # If the previously used character still has a remaining count, 
            # push it back to the heap now that an intervening character is placed
            if prev_count < 0:
                heapq.heappush(max_heap, [prev_count, prev_char])
                
            # Track the current character as the "previous" one for the next turn
            prev_count = count + 1  # reduce the actual frequency (since counts are negative)
            prev_char = char
            
        return "".join(result)
