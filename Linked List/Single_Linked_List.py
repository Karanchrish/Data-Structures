class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
        self.head2 = None
    def insert_at_beginning(self,newnode):
        if self.head:
            temp = self.head
            self.head = newnode
            self.head.next = temp
        else:
            self.head =newnode
    def insert_at_position(self,pos,newnode):
        if self.head:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.next
            newnode.next =temp.next
            temp.next =newnode
    def insert_at_end(self,newnode):
        if self.head:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
        else:
            self.head = newnode
    def delete_at_end(self):
        if self.head:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
        else:
            print("Not possible")
    def delete_at_position(self,pos):
        if self.head:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.next
            temp.next = temp.next.next
    def delete_at_beginning(self):
        if self.head:
            temp = self.head.next
            self.head = temp
        else:
            print("Not posible")
    def display(self):
        if self.head :
            temp = self.head
            while(temp != None):
                print(temp.data, end =  " ")
                temp = temp.next
        else:
            print("empty")
    def merge(self,head2):
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = head2
    def search(self,key):
        if self.head:
            temp = self.head
            c = 0
            while (temp != None):
                if(temp.data == key):
                    print("element is found")
                    c = 1
                temp = temp.next
            if c == 0:
                print("element is not found")
    def reverse(self):
       before = None
       temp = self.head
       while(temp is not None):
           next = temp.next
           temp.next = before
           before = temp
           temp = next
           self.head = before
    def sort(self):
        temp = self.head
        while(temp != None):
            current = temp.next
            while(current != None):
                if (temp.data > current.data):
                    temp.data,current.data = current.data,temp.data
                current = current.next
            temp = temp.next
    def length(self):
        if self.head:
            temp = self.head
            c = 0
            while(temp != None):
                c += 1
                temp = temp.next
            return c
               
q = LinkedList()
q.insert_at_beginning(node(11))
q.insert_at_beginning(node(21))
q.insert_at_position(1,node(31))
q.insert_at_position(2,node(41))
q.insert_at_end(node(51))
q.insert_at_end(node(61))
q.delete_at_beginning()
q.delete_at_end()
q.display()
print()
q.search(41)
q.reverse()
q.display()
print()
q.sort()
q.display()
print()
q.length()
q.display()
print()
q1 = LinkedList()
q1.insert_at_beginning(node(71))
q1.insert_at_beginning(node(81))
q1.insert_at_position(1,node(9))
q1.insert_at_position(2,node(11))
q1.insert_at_end(node(13))
q1.insert_at_end(node(14))
q1.delete_at_beginning()
q1.delete_at_end()
q1.display()
print()
q.merge(q1.head)
q.display()
print()