class Solution:
    def reverseString(self, s: List[str]) -> None:
        result = []
        
        for i in  range (len(s) - 1 , -1 , -1):
            result.append(s[i])
        for i in range(len(s)):
            s[i] = result[i]