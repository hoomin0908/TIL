arr = [5,4,1,2,7,8]
n = int(input())

for i in range(n) :
    for j in arr[::-1] :
        print(j,end=" ")
    print()