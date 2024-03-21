class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def EnQueue(self,newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear = newnode
        else:
            self.front = self.rear = newnode
            return
    def DeQueue(self):
        if self.front:
            t = self.front.data
            self.front = self.front.next
            return t
        elif(self.front == None):
            self.rear = None
        else:
            print("Queue is empty")
    def display(self):
        if self.front:
            temp = self.front
            while(temp!=None):
                print(temp.data,end=" ")
                temp = temp.next
            print()
q = Queue()
q.EnQueue(Node(10))
q.EnQueue(Node(20))
q.DeQueue()
q.EnQueue(Node(30))
q.EnQueue(Node(40))
q.EnQueue(Node(50))
q.DeQueue()
q.display()