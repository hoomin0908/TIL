def input_1() :
    global n
    n= list(map(int,input().split()))
def output_1():
    for i in n[::-1]:
        print(i,end="")

input_1()
output_1()