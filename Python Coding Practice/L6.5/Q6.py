a,b,c,d,e = input().split()
arr = [a,b,c,d,e]
result = 0
for i in arr :
    if i.isdigit() :
        result = result + 1

if result == 0:
    print('숫자미발견')
else :
    print(f'숫자{result}개발견')

