class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        # Map operators to their respective functions
        # int(a / b) correctly truncates toward zero in Python
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
                
        return stack[0]
