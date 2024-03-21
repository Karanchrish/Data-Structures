class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.capacity = size
        self.top = -1
    def push(self, val):
        if self.isFull():
            print('Stack Overflow')
        else:
            print('Push ',val,' to the stack')
            self.top = self.top + 1
            self.stack[self.top] = val
    def pop(self):
        if self.isEmpty():
            print('Stack Underflow')
        else:
            print('Pop ',self.peek(),' from the stack')
            top = self.stack[self.top]
            self.top = self.top - 1
            return top 
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.stack[self.top]
    def size(self):
        return self.top + 1
    def isEmpty(self):
        return self.size() == 0
    def isFull(self):
        return self.size() == self.capacity
stack = Stack(3) 
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
