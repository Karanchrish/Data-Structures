elements = list(map(int,input().split()))
n = len (elements)
print("iteration 0")
for i in range (0,n):
    for j in  range (i+1,n):
        if elements[i] > elements[j]:
            temp = elements[i]
            elements[i] = elements[j]
            elements[j] = temp
        print(elements)
    print("iteration",i+1)
    print(elements)
