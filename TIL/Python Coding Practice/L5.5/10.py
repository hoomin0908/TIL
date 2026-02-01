n = int(input())
arr = [n]
for i in range(5):
    arr.append(n*(i+2))

for j in arr:
    print(j,end=" ")