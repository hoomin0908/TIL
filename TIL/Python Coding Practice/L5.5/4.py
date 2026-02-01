n = int(input())
arr= []
arr.append(n)

for i in range(4):
    n = n-1
    arr.append(n)


def KFC() :
    for j in arr:
        print(j,end='')

KFC()