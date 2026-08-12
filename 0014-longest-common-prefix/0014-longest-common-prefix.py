# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         strs.sort()

#         first = strs[0]
#         last = strs[-1]
        
#         i = 0 

#         while i < min (len(first),len(last)) and first[i] == last[i]:
#             i += 1
#         return first [: i]





class Solution:
    def longestCommonPrefix(self,strs:List[str]) ->str:
        if not strs:
            return ""

        for i in range (len(strs[0])):
            current_char = strs [0][i]
            for word in strs [1: ]:
                if i == len(word) or word[i] != current_char:
                    return strs[0][:i]
        return strs[0]