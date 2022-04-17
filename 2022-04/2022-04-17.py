# 문제 1654 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = []

for _ in range(k):
    a.append(int(input()))

start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in a:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)