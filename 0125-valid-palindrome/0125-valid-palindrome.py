# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ""
#         for ch in s :
#             if ch.isalnum() :
#                 cleaned += ch.lower()
#         return cleaned == cleaned [:: -1]









class Solution:
    def isPalindrome(self, s: str) -> bool:
       left = 0 
       right = len (s)  - 1
       while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False  # Not a palindrome
            
            left += 1   # Move left pointer inward
            right -= 1  # Move right pointer inward

       return True  #
   