arr = []
a,b,c = map(int,input().split())
n = int(input())

arr.extend([a,b,c,n])

for i in range(2):
    n = n+1
    arr.append(n)
for j in arr :
    print(j,end=" ")

