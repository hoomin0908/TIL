a,b = map(int,input().split())
def BBQ(x,y):
    Sum = x+y
    Minus = x-y
    times = x*y
    dev = a/b
    return Sum, Minus,times,dev

print(BBQ(a,b))
