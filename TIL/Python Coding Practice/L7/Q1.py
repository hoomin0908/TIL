arr1 = [3,5,2,4,1]
arr2 = [[9,8],[7,1],[3,4]]
n = int(input())

if n%2 ==1 :
    for i in arr1 :
        print(i, end="")
elif n%2 == 0 :
    for w in arr2 :
        for j in w :
            print(j,end="")
        print()