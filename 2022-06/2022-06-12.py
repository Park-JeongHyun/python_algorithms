# 문제 2443 별 찍기 - 6

n = int(input())

for i in range(n):
    print(" " * i + "*" * (2 * (n-i) - 1) )