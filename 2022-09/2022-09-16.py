# 문제 10103 주사위 게임

n = int(input())

a = 100
b = 100

for _ in range(n):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        b -= num1
    elif num1 < num2:
        a -= num2
    else:
        continue

print(a)
print(b)