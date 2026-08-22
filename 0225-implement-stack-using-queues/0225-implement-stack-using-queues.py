class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # Add the new element to the back
        self.q.append(x)
        # Rotate the queue to bring the new element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The front of the queue is the top of the stack
        return self.q.popleft()

    def top(self) -> int:
        # Look at the front element without removing it
        return self.q[0]

    def empty(self) -> bool:
        # Check if the queue has no elements
        return not self.q
