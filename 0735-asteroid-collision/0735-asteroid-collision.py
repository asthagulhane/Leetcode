class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            # Collision only happens if the current asteroid moves left (< 0) 
            # and the previous asteroid in the stack moves right (> 0)
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()  # Top asteroid explodes, check next one
                    continue
                elif stack[-1] == -a:
                    stack.pop()  # Both asteroids explode
                break            # Current asteroid explodes or both exploded
            else:
                stack.append(a)  # Current asteroid survives or no collision occurs
                
        return stack
