class Solution:
    def isValid(self, s: str) -> bool:
        # Keep replacing pairs until no more changes happen
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]" ,"")
            
        return s == ""

        