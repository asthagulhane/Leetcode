class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.front = 0 
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[(self.front + self.size) % self.capacity] = value
        self.size +=1
        return True    

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True   
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[(self.front + self.size - 1) % self.capacity]    
        
    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.capacity
        


