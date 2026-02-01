arr = [4,1,2,3,5]
n = input()

if n == 'a'or n == 'b' or n == 'c':
    for i in arr[3::-1]:
        print(i,end=" ")
else :
    for j in arr[4:0:-1]:
        print(j, end=" ")