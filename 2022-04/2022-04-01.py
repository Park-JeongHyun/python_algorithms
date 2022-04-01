# 문제 10773 제로

import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []

for _ in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i] != 0:
        b.append(a[i])
    if a[i] == 0:
        b.pop()

print(sum(b))