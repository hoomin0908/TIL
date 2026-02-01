def input_1() :
    global a,b
    a,b = map(int,input().split())
    
def output_1() :
    s = a+b
    i = 5
    while i <= s:
        print(i,end=" ")
        i +=1 


input_1()
output_1()