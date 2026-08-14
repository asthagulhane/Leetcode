# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(s.split()[:: -1])
        




class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = len(s) - 1

        while i >= 0:
            # skip the spaces
            while i >= 0 and s[i] == ' ' :
                i -= 1 
            if i< 0:
                break 
                     
            end = i 

            while i >= 0 and s [i] != ' ': 
                i -= 1

            words.append(s[i + 1: end  + 1])

        return " ".join(words)