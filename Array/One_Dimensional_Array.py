class array:
    def __init__(self):
        self.arr=[]
        self.n=0

    def insertion_at_beginning(self,element):
        print("inserting")
        self.arr+=[None]
        self.n+=1
        for i in range(self.n-1,0,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[0]=element
        print(self.arr)

    def insertion_at_position(self,element,position):
        if(position>self.n):
            print('Position not possible to insert')
            return
        print("inserting")
        self.arr+=[None]
        self.n+=1
        for i in range(self.n-1,position-1,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[position-1]=element
        print(self.arr)

    def insertion_at_end(self,element):
        print("inserting")
        self.arr+=[None]
        self.n+=1
        self.arr[self.n-1]=element
        print(self.arr)

    def deletion_at_beginning(self):
        print("deleting")
        del self.arr[0]
        self.n-=1
        print(self.arr)

    def deletion_at_end(self):
        print("deleting")
        del self.arr[self.n-1]
        self.n-=1
        print(self.arr)

    def deletion_at_position(self,pos):
        if(pos>self.n):
            print('index not found,unable to delete')
            return
        print("deleting")
        del self.arr[pos-1]
        self.n-=1
        print(self.arr)

    def Update(self,key,value):
        print("updation")
        temp=self.Search(key)
        print(int(temp))
        if(temp==-1):
            print('Element not found')
            return
        else:
            self.arr[temp]=value

    def Search(self,key):
        print("Searching")
        for i in range(0,self.n):  
            if (self.arr[i] == key):  
                print('Element ',str(key),' found at index '+str(i))
                return i
        return -1

    def Sort(self):
        print("Sorting")
        for i in range(0,self.n-1):
            for j in range(self.n-1):
                if(self.arr[j]>self.arr[j+1]):
                    temp=self.arr[j]
                    self.arr[j]=self.arr[j+1]
                    self.arr[j+1]=temp
        print("Array after sorting",self.arr)  

      
arr=array()
arr.insertion_at_beginning(2)
arr.insertion_at_beginning(5)
arr.insertion_at_beginning(3)
arr.insertion_at_end(7)
arr.insertion_at_beginning(13)
arr.insertion_at_end(907)
arr.insertion_at_beginning(243)
arr.insertion_at_position(8,3)
arr.insertion_at_position(2,4)
arr.deletion_at_beginning()
arr.deletion_at_end()
arr.deletion_at_position(3)
arr.deletion_at_position(20)
arr.Sort()
arr.Search(5)