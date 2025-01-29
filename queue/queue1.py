class Queue:
    def __init__(self):
        self.values = [] 

    def enqueue(self, x):
       
        self.values.append(x)

    def dequeue(self):
       
        if not self.values:
            return "Queue is empty"  
        front = self.values[0]
        self.values = self.values[1:] 




q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Queue after enqueues:", q1.values)  

q1.enqueue(40)
print("Queue after another enqueue:", q1.values)  
dequeued = q1.dequeue()
print("Dequeued element:", dequeued) 
print("Queue after dequeue:", q1.values)  