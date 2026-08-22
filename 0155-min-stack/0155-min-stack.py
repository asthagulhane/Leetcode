class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Store (val, minimum_so_far)
        curr_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
