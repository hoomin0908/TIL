n = map(int,input().split())
for i in n :
    if 20>i :
        print('더 큰수를 입력하세요')
    if 20<i :
        print('더 큰수를 입력하세요')
    if i == 20 :
        print('정답입니다')