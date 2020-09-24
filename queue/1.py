# Array implementation Of Queue

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

    def qDisplay(self):
        for i in range(self.size):
            print(self.queue[i])


if __name__ == "__main__":
    capacity = int(input('Enter the capacity of the queue : '))
    newQueue = Queue(capacity)
    choice = '-1'
    while(choice != '4'):
        print("------------------------------------\n")
        print("    QUEUE IMPLEMENTATION PROGRAM    \n")
        print("------------------------------------\n")
        print("1. Enqueue\n")
        print("2. Dequeue\n")
        print("3. Front\n")
        print("4. Exit\n")
        print("5. Rear\n")
        print("6. Display\n")
        print("------------------------------------\n")
        choice = (input("Enter your choice: "))

        if(choice == '1'):
            newQueue.enQueue()
        elif(choice == '2'):
            newQueue.deQueue()
        elif(choice == '3'):
            newQueue.qFront()
        elif(choice == '4'):
            choice = '4'
        elif(choice == '5'):
            newQueue.qRear()
        elif(choice == '6'):
            newQueue.qDisplay()
        else:
            print('Invalid INPUT! Try again')
