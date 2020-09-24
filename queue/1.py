class Queue:

    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.queue = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0
