a,b = map(int,input().split())
if 30<a*b<50 :
    print('적당한 사이즈')
elif a*b>50 :
    print('큰 사이즈')
elif 30>a*b :
    print('작은 사이즈')