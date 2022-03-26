# 문제 1920 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

m = int(input())
b = list(map(int, input().split()))

def solve(s):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == s:
            return True

        if s < a[mid]:
            right = mid-1
        elif s > a[mid]:
            left = mid + 1

for i in b:
    if solve(i):
        print(1)
    else:
        print(0)