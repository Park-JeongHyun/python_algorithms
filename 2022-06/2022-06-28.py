# 문제 10991 별 찍기 - 16

n = int(input())

for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))