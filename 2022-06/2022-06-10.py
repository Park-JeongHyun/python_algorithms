# 문제 2444 별 찍기 - 7

n = int(input())

for i in range(n-1, -1, -1):
    print(" " * i + "*" * (n - i) + "*" * (n - i - 1))

for i in range(1, n):
    print(" " * i + "*" * (n - i) + "*" * (n - i - 1))