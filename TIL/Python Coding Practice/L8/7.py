arr1 = ['B','D',5,'Q','A']
arr2 = ['Q','E','R','E','F']

def input_1() :
    global n
    n = input()

def output():
    global n, arr1, arr2
    if n.islower() :
        for i in arr1:
            print(i,end="")
    if n.isupper() :
        for j in arr2:
            print(j,end="")
    if n.isdigit():
        print('HGFEDCBA')

input_1()
output()