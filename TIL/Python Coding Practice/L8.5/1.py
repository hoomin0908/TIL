arr = []
for _ in range(6):
    n = map(int,input().split())
    arr.append(n)

for i in range(6):
    if arr[i] < 5:
        print(f'{i}번은 {arr[i]}점 불합격')
    if arr[i]>=5 :
        print(f'{i}번은 {arr[i]}점 합격')