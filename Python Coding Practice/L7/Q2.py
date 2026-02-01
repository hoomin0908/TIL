a, b = map(int,input().split())
if a > b :
    n = a - b

if b > a :
    n = b - a

if n%2 == 1 :
    print('고백한다')
else :
    print('짝사랑만')