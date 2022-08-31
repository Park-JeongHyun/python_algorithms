# 문제 2605 줄 세우기

n = int(input())

a = list(map(int, input().split()))

for i in range(n):
    a.insert(i - a[i], i+1)
    del a[i + 1]

print(*a)