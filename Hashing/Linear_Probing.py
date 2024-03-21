H=[]
M=10
for i in range(M):
    H.append(None)
def insert():
    key = int(input("\n Enter the Value to Insert : "))
    for i in range(M):
        hf = (key+i)%M
        if (H[hf]==None):
            H[hf] = key
            break
    if(i==M-1):
        print("Hash Table is Full")
def search():
    key = int(input("\n Enter the Value to Search : "))
    for i in range(M):
        hf = (key+i)%M
        if (H[hf]==key):
            print("Element Found")
            break
    if(i==M-1):
        print("Key is not found in Hash Table")
def display():
    for i in range(M):
        print("{} position => {} value".format(i,H[i]))
while(1):
    print("\n 1.Insert 2.Search 3.Display 4.Quit \n")
    opt = int(input())
    if(opt==1):
        insert()
    elif(opt==2):
        search()
    elif(opt==3):
        display()
    elif(opt==4):
        break