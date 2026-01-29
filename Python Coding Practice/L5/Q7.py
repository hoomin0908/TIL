a,b,c = map(int,input().split())
arr = [0]*6
arr[0],arr[1],arr[2] = a,b,c

d = int(input())
arr[3],arr[4],arr[5]= d,d+1,d+2


for i in range(6) :
    print(arr[i],end=" ")
