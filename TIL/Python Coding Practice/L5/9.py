arr = ['A','B','C']
def KFC() :
    for i in arr:
        print(i,end="")
def main() :
    global n
    n = int(input())
    for _ in range(n):
        KFC()
        print()

main()