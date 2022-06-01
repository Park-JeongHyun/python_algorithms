# 문제 10815 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))
a.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(a, b[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')