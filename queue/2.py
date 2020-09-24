class CircularQueue:

    def __init__(self, capacity):
        self.size = capacity
        self.queue = [None]*capacity
        self.front = self.rear = -1

    def enqueue(self):
        data = input('Enter the data : ')

        # Check if queue is full
        if((self.rear + 1) % self.size == self.front):
            print('Queue is FULL')

        # If queue is empty
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        # If queue is not empty
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
