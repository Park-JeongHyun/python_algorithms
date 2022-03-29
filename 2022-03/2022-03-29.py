# 문제 10814 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    age, name = input().split()
    a.append([int(age),name])

a.sort(key=lambda x : x[0])
for i in range(n):
    print(*a[i])