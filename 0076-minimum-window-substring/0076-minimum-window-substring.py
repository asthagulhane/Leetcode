# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_count = Counter(t)
#         res = ""
        
#         # Check every possible substring
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 sub = s[i:j+1]
                
#                 # Counter comparison checks if sub contains all elements of t
#                 if not (t_count - Counter(sub)):
#                     if not res or len(sub) < len(res):
#                         res = sub
                        
#         return res

 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s):
            # 1. Expand the window
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            # 2. Shrink the window if it contains all characters
            while missing == 0:
                if end == 0 or (right - left + 1) < (end - start):
                    start, end = left, right + 1
                
                # Remove the leftmost character and update counts
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
                
        return s[start:end]
