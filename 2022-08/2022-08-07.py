# 문제 2476 주사위 게임

n = int(input())

result = 0

for _ in range(n):
    a = []
    d1, d2, d3 = map(int, input().split())
    a.append(d1)
    a.append(d2)
    a.append(d3)

    if d1 == d2 == d3:
        temp = 10000 + d1 * 1000
        if temp > result:
            result = temp
    elif d1 == d2:
        temp = 1000 + d1 * 100
        if temp > result:
            result = temp
    elif d2 == d3:
        temp = 1000 + d2 * 100
        if temp > result:
            result = temp
    elif d1 == d3:
        temp = 1000 + d3 * 100
        if temp > result:
            result = temp
    elif d1 != d2 and d2 != d3 and d1 != d3:
        temp = max(a) * 100
        if temp > result:
            result = temp

print(result)