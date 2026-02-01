n = int(input())
arr = [n,n-1,n-2,n-3,n-4]

def KFC() :
    for i in range(5) :
        print(arr[i], end="")

KFC()