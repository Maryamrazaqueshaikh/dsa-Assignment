class Queue(object):
    def __init__(self, limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def __str__(self):
        return ''.join([str(i) for i in self.queue])

    def enqueue(self, data):
        if self.size >= self.limit:
            return -1  
        else:
            self.queue.append(data)

            if self.front is None:
                self.front = 0

            self.rear = self.size
            self.size += 1

    def isEmpty(self):
        return self.size <= 0

    def dequeue(self):
        if self.isEmpty():
            return -1  

        dequeued_item = self.queue.pop(0)  
        self.size -= 1

        if self.size == 0:
            self.front = self.rear = None  
        else:
            self.front = 0  
            self.rear = self.size - 1  

        return dequeued_item  

    def getSize(self):
        return self.size

if __name__ == '__main__':
    myQueue = Queue()

    myQueue.enqueue(19)
    myQueue.enqueue(16)
    myQueue.enqueue(14)
    myQueue.enqueue(18)
    print(myQueue)  

    print(f'Size: {myQueue.getSize()}')  

    myQueue.dequeue()  
    print(myQueue)  
    print(f'Size: {myQueue.getSize()}') 