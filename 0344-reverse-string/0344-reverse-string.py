# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         result = []
        
#         for i in  range (len(s) - 1 , -1 , -1):
#             result.append(s[i])
#         for i in range(len(s)):
#             s[i] = result[i]



class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0 
        right = len(s)  - 1 

        while left < right:
            s[left] , s[right] = s[right],s[left]
        
            left += 1
            right -= 1