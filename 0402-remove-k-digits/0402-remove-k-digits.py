class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            # Pop elements from stack if the current digit is smaller than the top
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k is still > 0, remove digits from the end
        final_stack = stack[:-k] if k > 0 else stack
        
        # Join and strip leading zeros, return "0" if empty
        return "".join(final_stack).lstrip('0') or "0"
