ch1,ch2 = input().split()
for t in range(4) :
    for i in range(ord(ch1),ord(ch2)+1) :
        print(chr(i),end=" ")
    print()
