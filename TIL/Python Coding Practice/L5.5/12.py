n = list(map(int,input().split()))
num= 0
for i in n :
    num = i + num
print(f'합은 {num}입니다')