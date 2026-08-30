import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        # Swap the element to delete with the last element
        idx, last_element = self.pos[val], self.data[-1]
        self.data[idx] = last_element
        self.pos[last_element] = idx
        # Remove the last element
        self.data.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
