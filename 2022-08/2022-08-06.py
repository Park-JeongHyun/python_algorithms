# 문제 1547 공

n = int(input())
temp = 1

for _ in range(n):
    x, y = map(int, input().split())

    if x == temp:
        temp = y
    elif y == temp:
        temp = x

print(temp)