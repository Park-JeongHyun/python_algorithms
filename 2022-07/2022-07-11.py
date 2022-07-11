# 문제 10797 10부제

n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i >= 30:
        i -= 30
    elif i >= 20:
        i -= 20
    elif i >= 30:
        i -= 30

print(a.count(n))