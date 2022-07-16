# 문제 2902 KMP는 왜 KMP일까?

a = list(input())

print(a[0], end='')

for i in range(len(a)):
    if a[i] == '-':
        print(a[i+1], end='')