main = int(input())

arr = ['A','B','C']

def KFC():
    result = ""
    for i in range(3):
        result += arr[i]
    return result

for _ in range(main):
    print(KFC())

