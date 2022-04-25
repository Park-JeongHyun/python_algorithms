# 문제 1927 최소 힙

import sys
import heapq
input = sys.stdin.readline

a = []
n = int(input())

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(a) == 0:
            print(0)
        else:
            print(heapq.heappop(a))
    else:
        heapq.heappush(a, num)
