# 문제 11651 좌표 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key = lambda x:(x[1],x[0]))
for i in range(n):
    print(*a[i])