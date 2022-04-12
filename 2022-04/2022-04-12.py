# 문제 2805 나무자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

start, end = 1, max(t)

while start <= end:
     mid = (start + end) // 2

     tree = 0
     for i in t:
          if i >= mid:
               tree += i-mid

     if tree >= m:
          start = mid + 1
     else:
          end = mid - 1

print(end)