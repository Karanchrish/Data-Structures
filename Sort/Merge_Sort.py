def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            array[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
def printlist(array):
    for i in range(len(array)):
        print(array[i],end= " ")
    print()
print("Enter a Array :")
array = list(map(int , input().split()))
mergeSort(array)
print("The Sorted Array is :")
printlist(array)