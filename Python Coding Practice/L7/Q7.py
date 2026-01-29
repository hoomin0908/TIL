a,b,c = map(int,input().split())
if a > b and a > c :
    MAX = a
if b > a and b > c :
    MAX = b
if c >a and c >b :
    MAX = c
if a < b and a < c :
    MIN = a
if b < a and b < c :
    MIN = b
if c <a and c < b :
    MIN = c





print(f'MAX={MAX}')
print(f'MIN={MIN}')