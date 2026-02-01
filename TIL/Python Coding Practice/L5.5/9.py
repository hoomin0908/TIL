a,b = map(int,input().split())
arr = [a]
for i in range(4):
    a = a+b
    arr.append(a)

for j in arr:
    print(j,end=" ")