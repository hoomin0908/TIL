n = list(map(int,input().split()))
arr=[]
k = 0

for i in range(3) :
    row = []
    for j in range(2):
        row.append(n[k]+2)
        k+=1
    arr.append(row)

for i in range(3) :
    for j in range(2):
        print(arr[i][j],end=" ")
    print()