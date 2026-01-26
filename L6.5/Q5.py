a,b,c = map(int,input().split())
arr = [a,b,c]
for i in range(a+b+c) :
    for j in arr :
        print(j,end=" ")
    print()