class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,newnode):
        if self.top:
            temp = self.top
            self.top = newnode
            self.top.next = temp
        else:
            self.top = newnode
    def pop(self):
        if self.top:
            t=self.top
            self.top = self.top.next
            return t.data
        else:
            print("Linked list is Empty")
    def peek(self):
        if self.top:
            return self.top.data
        else:
            print("Linked list is empty")
n = Stack()
n.push(Node(1))
n.push(Node(2))
n.push(Node(3))
print("The popped element is ",n.pop())
print("The peek element is ",n.peek())
