arr = list(map(int,input().split()))
cnt = 0
for i in arr :
    if 3<=i<=7 :
        cnt = cnt + 1 
print(cnt)