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
        res = '' 

        for i in range (len(strs[0])):
            for s  in  strs :
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res