price = int(input())

def starBox() :
    for i in range(1,21):
        if i%2 == 0:
            continue
        print(i,end=" ")

def macDoll() :
    for j in range(72,64,-1):
        print(chr(j),end=" ")

def copyBean() :
    for p in range(-5,6):
        print(p,end=" ")

if 3500<=price<=5000 :
    starBox()

elif 2500<=price<3500:
    macDoll()

else :
    copyBean()