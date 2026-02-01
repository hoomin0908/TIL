arr1 = [0]*5
arr2 = [0]*5
a,b,c,d,e = map(int,input().split())
arr1 = arr2 = [a,b,c,d,e]

for i in range(5) :
    print(arr1[i], end="")

print()

for i in range(5) :
    print(arr2[i], end="")