class Solution:
    def calculate(self, s: str) -> int:
        # Remove whitespace to avoid inner loop edge cases
        s = s.replace(" ", "")
        
        current_num = 0
        last_num = 0
        total_sum = 0
        sign = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            # Process operator or final character
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    total_sum += last_num
                    last_num = current_num
                elif sign == '-':
                    total_sum += last_num
                    last_num = -current_num
                elif sign == '*':
                    last_num = last_num * current_num
                elif sign == '/':
                    # int() handles truncation toward zero for both positive and negative results
                    last_num = int(last_num / current_num)
                    
                sign = char
                current_num = 0
                
        return total_sum + last_num
