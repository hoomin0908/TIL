arr=[]
for i in range(2) :
    row= []
    for j in range(4):
        row.append(0)
    arr.append(row)

y,x = map(int, input().split())

arr[y][x] = 1

for row in arr :
        print(*row,sep=" ")