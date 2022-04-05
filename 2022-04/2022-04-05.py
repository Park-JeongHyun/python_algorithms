# 문제 1874 스택수열

n = int(input())

a = []
b = []

cnt = 1
temp = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        a.append(cnt)
        cnt += 1
        b.append('+')
    if a[-1] == num:
        a.pop()
        b.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in b:
        print(i)
