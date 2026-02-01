arr = [[0]*3 for _ in range(2)]

def input_01() :
    global arr
    nums = list(map(int, input().split()))
    idx = 0
    for i in range(2):
        for j in range(3):
            arr[i][j] = nums[idx]
            idx += 1

def process() :
    global total
    total = 0
    for i in range(2):
        for j in range(3):
            total += arr[i][j]

def output():
    print(total)

input_01()
process()
output()

