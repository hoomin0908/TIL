a,b,c,d = map(int,input().split())
arr = [a,b,c,d]
total = 0

for i in range(4) :
    total = total + int(arr[i])

print(total)
