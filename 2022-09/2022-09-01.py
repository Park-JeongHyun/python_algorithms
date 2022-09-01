# 문제 2693 N번 째 큰 수

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    print(a[-3])