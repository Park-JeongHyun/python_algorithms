# 문제 18870 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = sorted(set(a))

dict = {b[i] : i for i in range(len(b))}

for i in a:
    print(dict[i], end=' ')