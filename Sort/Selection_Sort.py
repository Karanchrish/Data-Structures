elements=list(map(int,input().split()))
n=len(elements)
for i in range(0,n):
  min=i
  print("ITERATION",i)
  for j in range(i+1,n):
    if elements[min]>elements[j]:
      min=j
  if(min!=i):
    elements[min],elements[i]=elements[i],elements[min]
  print(elements)
