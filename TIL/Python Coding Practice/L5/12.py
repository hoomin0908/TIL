def QTR() :
    print('QTR100%')
def BBQ() :
    print('BBQ100%')

arr = list(map(int,input().split()))
n = 0
for i in arr :
    n = i + n
if n >= 10 :
    QTR()
else :
    BBQ()
