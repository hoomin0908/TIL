char1 = []
char2 = []

n = input()

for i in range(5):
    print(chr(ord(n) + i),end="")
print()


for i in range(5):
    print(chr(ord(n) - i),end="")
