class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the multi-digit multiplier
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push current state to stack and reset
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif char == ']':
                # Pop previous state and multiply the enclosed string
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                # Append standard characters
                curr_str += char
                
        return curr_str
