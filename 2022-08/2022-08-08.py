# 문제 10990 별 찍기 - 15

n = int(input())

for i in range(n):
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 1)
    if i == 0 else (" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*"))