# 문제 10995 별 찍기 - 20

n = int(input())

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)