flag = 0
a = b = c = ''

def input_1():
    global a, b, c
    a, b, c = input().split()

def process():
    global flag
    if a == 'A' and b == 'B' and c == 'C':
        flag = 1

def output():
    if flag == 1:
        print('ABC를찾았다')
    else:
        print('못찾았다')

input_1()
process()
output()