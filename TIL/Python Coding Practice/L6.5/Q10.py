A,B,C = input().split()
arr = [A,B,C]
if ord(A) > ord(B) and ord(A)>ord(C) :
    print(f'옳다{A}')
else :
    print('옳지않음')