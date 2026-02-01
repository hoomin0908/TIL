a,b,c = map(int, input().split())
arr = [a,b,c]
n = int(input())
arr = [a,b,c,n]
for i in range(2):
    n = n+1
    arr.append(n)

for j in arr :
    print(j,end=" ")
