arr = [[0]*4 for _ in range(3)]

def input_1():
    global arr
    n = int(input())
    cnt = n
    for i in range(3):
        for j in range(4):
            arr[i][j]= cnt
            cnt += 1

def process() :
    global arr
    for i in range(3):
        for j in range(4):
            arr[i][j] += 1

def output() :
    global arr
    for i in arr:
        for j in i :
            print(j , end=" ")
        print()



input_1()
process()
output()