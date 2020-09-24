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

    def enQueue(self):
        item = input('Enter the data : ')
        if self.isFull():
            print('Queue is FULL')
            return

        self.rear = (self.rear + 1) % (self.capacity)
        self.queue[self.rear] = item
        self.size += 1
        print('{} Enqueued '.format(item))

    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        print('{} Dequeued'.format(self.queue[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size -= 1

    def qFront(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        print('FRONT : {}'.format(self.queue[self.front]))

    def qRear(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        print('REAR : {}'.format(self.queue[self.rear]))
