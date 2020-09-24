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

    def dequeue(self):

        # If queue is empty
        if(self.front == -1):
            print('Queue is EMPTY')

        # If there is only one element in the QUEUE
        elif(self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print('Data POPPED {}'.format(temp))

        # If there is more than one element in the queue
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print('Data POPPED {}'.format(temp))
