a,b = map (int, input().split())
arr = [0]*6

for i in range(b - a + 1):
    arr[i] = a + i

for t in arr :
    if t != 0:
        print(t, end="")
