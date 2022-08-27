# 문제 9085 더하기

n = int(input())

for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    print(sum(a))