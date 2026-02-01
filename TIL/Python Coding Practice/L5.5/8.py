a,b = map(int,input().split())
arr = [a]
for i in range(2):
    a = a+1
    arr.append(a)
arr.append(b)
for j in range(2):
    b = b-1
    arr.append(b)
arr[3:6]=reversed(arr[3:6])
for m in arr :
    print(m,end=" ")