class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0 
        max_length = 0 
        def expand(left,right):
            nonlocal start ,max_length

            while left >= 0 and right < len(s) and  s[left] == s[right]:
                if right - left + 1 >max_length :
                    start = left
                    max_length = right - left + 1 
                left  -= 1
                right += 1
        for i in range (len(s)):
            expand(i,i )
            expand (i, i + 1)
        return s[start :start + max_length ]

       

      