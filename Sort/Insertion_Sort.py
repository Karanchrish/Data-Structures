def insertionSort(arr):
    for i in range(n):
        print("ITERATION",i)
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
        print(arr)
arr = list(map(int,input().split()))
n = len(arr)
insertionSort(arr)
