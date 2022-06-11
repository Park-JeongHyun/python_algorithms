# 문제 11286 절댓갑 힙

import sys
import heapq
input = sys.stdin.readline
a = []
n = int(input())

def order():
    num = int(input())
    if num == 0:
        if len(a) == 0:
            print(0)
        else:
            print(heapq.heappop(a)[1])
    elif num != 0:
        heapq.heappush(a, (abs(num), num))

for i in range(n):
    order()
