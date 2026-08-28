class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating in both orders doesn't match, there is no common divisor
        if str1 + str2 != str2 + str1:
            return ""
        # The length of the GCD string is the mathematical GCD of the two lengths
        gcd_len = math.gcd(len(str1), len(str2))

        # Return the prefix of that length
        return str1[:gcd_len]
