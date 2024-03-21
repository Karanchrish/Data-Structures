class queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.capacity=size
        self.front=-1
        self.rear=-1
    def enqueue(self,value):
        if(self.front==-1 and self.rear==-1):
            self.front=self.rear=0
            self.queue[self.rear]=value
            print("The Enqueue Value is :",value)
        else:
            if(self.rear==self.capacity-1):
                print("Queue is Full")
                return
            else:
                self.rear+=1
                self.queue[self.rear]=value
                print("The Enqueue Value is :",value)
    def dequeue(self):
        if(self.front==-1 and self.rear==-1):
            print("Queue is Empty")
            return
        elif(self.front==self.rear):
            self.front=self.rear=-1
        else:
            Temp=self.queue[self.front]
            self.front+=1
            print("The Dequeue Value is :",Temp)
    def display(self):
        for i in range(self.front,self.capacity,1):
            print("Displayed Element is :",self.queue[i])
    def peek(self):
        print(" **The Peek Element is** :",self.queue[self.front])
    def size(self):
        print(" *The Size of the Queue* :",self.rear+1-self.front)
Q=queue(5)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.peek()
Q.size()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.display()
Q.peek()
Q.size()
