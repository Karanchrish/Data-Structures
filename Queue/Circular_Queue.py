class Circular_Queue :
    def __init__(self,size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.capacity = size
    def enqueue(self,value):
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            return
        if (self.rear+1)%self.capacity == self.front :
            print("Queue is full")
            return
        else:
            self.rear = (self.rear+1)%self.capacity
            self.queue[self.rear] = value
            return
    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty")
            return
        if self.front == self.rear :
            temp = self.queue[self.front]
            self.front = self.rear = 0
            return temp
        else :
            temp = self.queue[self.front]
            self.front = (self.front+1)%self.capacity
            return temp

    def display(self):
        if self.front == -1 and self.rear == -1 :
            print("Queue is empty")
            return
        i = self.front
        while(True):
            print(self.queue[i])
            if i == self.rear :
                break
            i = (i+1)%self.capacity
        return
q = Circular_Queue(6)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.display()
