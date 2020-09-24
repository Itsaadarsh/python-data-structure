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

    def displayQueue(self):

        if(self.front == -1):
            print('Queue is EMPTY')

        elif(self.rear >= self.front):
            print('Elements are : ')
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")

        else:
            print('Elements are : ', end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        if((self.rear + 1) % self.size == self.front):
            print('\n\nQueue is FULL')


if __name__ == "__main__":
    capacity = int(input('Enter the capacity of the queue : '))
    newQueue = CircularQueue(capacity)
    choice = '-1'
    while(choice != '4'):
        print("\n\n------------------------------------\n")
        print("    QUEUE IMPLEMENTATION PROGRAM    \n")
        print("------------------------------------\n")
        print("1. Enqueue\n")
        print("2. Dequeue\n")
        print("3. Display\n")
        print("4. Exit\n")
        print("------------------------------------\n")
        choice = (input("Enter your choice: "))

        if(choice == '1'):
            newQueue.enqueue()
        elif(choice == '2'):
            newQueue.dequeue()
        elif(choice == '3'):
            newQueue.displayQueue()
        elif(choice == '4'):
            choice = '4'
        else:
            print('Invalid INPUT! Try again')
