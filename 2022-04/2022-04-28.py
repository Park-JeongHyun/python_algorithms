# 문제 11279 최대 힙

import sys
import heapq
input = sys.stdin.readline
a = []

n = int(input())

for _ in range(n):
    x = int(input())

    if x == 0:
        if len(a) == 0:
            print(0)
        else:
            print(heapq.heappop(a)*-1)
    else:
        heapq.heappush(a, -x)
