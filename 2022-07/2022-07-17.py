# 문제 9093 단어 뒤집기

n = int(input())

a = []
for i in range(n):
    a.append(input().split())

for i in a:
    for j in i:
        for k in range(len(j)-1, -1, -1):
            print(j[k], end='')
        print(' ', end='')
    print()