arr = list(map(int, input().split()))

def QTR():
    print('QTR100%')

def BBQ():
    print('BBQ100%')

result = 0
for i in arr:
    result += i  
    if result >= 10:
        QTR()
    else:
        BBQ()

