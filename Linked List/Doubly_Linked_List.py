class Node:
    def __init__(self,val):
        self.prev = None
        self.data = val
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beg(self,newnode):
        if self.head:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        else:
            self.head = newnode
    def insert_at_end(self,newnode):
        if self.head:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
            newnode.next = None
        else:
            self.head = newnode
    def insert_at_pos(self,pos,newnode):
        if(self.head):
            temp = self.head
            for i in range(0,pos-2):
                temp = temp.next
            newnode.next = temp.next
            temp.next.prev = newnode
            temp.next = newnode
            newnode.prev = temp
        else:
            self.head = newnode
    def delete_at_end(self):
        if self.head:
            temp = self.head
            while(temp.next.next!=None):
                temp = temp.next
            temp.next = None
        else:
            print("Linked list is empty")
    def delete_at_beg(self):
        if self.head:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        else:
            print("Linked list is empty")
    def delete_at_pos(self,pos):
        if self.head:
            temp1=self.head
            for i in range(1,pos-2):
                temp = temp.next
            temp2 = temp1.next
            temp1.next = temp2.next
            temp2.next.prev = temp1
            temp2.prev = None
        else:
            print("Linked list is empty")
    def display(self):
        if self.head:
            temp = self.head
            while(temp!=None):
                print(temp.data,end=' ')
                temp = temp.next
            print()
        else:
            print("Linked list is empty")
l=DoublyLinkedList()
l.insert_at_beg(Node(10))
l.insert_at_end(Node(90))
l.insert_at_end(Node(80))
l.insert_at_end(Node(50))
l.insert_at_end(Node(70))
l.insert_at_end(Node(30))
l.insert_at_pos(2,Node(40))
l.display()
l.delete_at_end()
l.delete_at_beg()
l.delete_at_pos(2)
l.display()
