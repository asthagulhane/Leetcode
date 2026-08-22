class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = [0] * 26, [0] * 26
        for c in s1:
            c1[ord(c) - 97] += 1
            
        for i, c in enumerate(s2):
            c2[ord(c) - 97] += 1
            if i >= len(s1):
                c2[ord(s2[i - len(s1)]) - 97] -= 1
            if c1 == c2:
                return True
                
        return False

        