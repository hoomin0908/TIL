lst = [list(map(int,input().split())) for _ in range (6)]
cnt = 0
for i in range(6):
    if lst[i][0]<lst[i][1]:
        lst[i][0],lst[i][1]= lst[i][1],lst[i][0]
        cnt+=1

for j in lst :
    print(*j)

    print(f'{cnt}명')
