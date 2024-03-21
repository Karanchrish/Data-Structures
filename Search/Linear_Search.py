def linear_search(arr,key):
    n = len(arr)
    c = -1
    for i in range (n):
        if arr[i] == key:
            c = i
            break
    if c > -1:
        print(key,"found at",c)
    else:
        print(key,"element not found")
arr = list(map(int,input("Enter the Array :").split()))
key = int(input("Enter the key to search :"))
linear_search(arr,key)


##########################################################################################

def r_linear_search(arr,n,key):
    if n == -1:
        return False
    if arr[n] ==key:
        return n
    return r_linear_search(arr,n-1,key)
arr = list(map(int,input("Enter the Array :").split()))
key = int(input("Enter the key to search :"))
n = len(arr)
res= r_linear_search(arr,n-1,key)
if res > -1:
    print(key,"found at",res)
else:
    print("element not found")
