def binary_search(arr,x):
    low=0
    high=len(arr)
    while low<=high:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high = mid-1
    return False
arr=list(map(int,input().split()))
x=int(input("Enter the key to search:"))
result=binary_search(arr,x)

if result != -1:
    print("Element is present at index",result)
else:
    print("Element not present")

#################################################################################################

def recbinary_search(arr,low,high,key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return recbinary_search(arr,low,mid - 1,key)
        else:
            return recbinary_search(arr,mid + 1,high,key)
    else:
        return -1
arr = list(map(int,input().split()))
key = int(input("Enter the element to search : "))
n = len(arr)
i = recbinary_search(arr,0,n-1,key)
if i != -1:
    print(key," element found at index = ", i)
else:
    print("Element not found")
