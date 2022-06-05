# 문제 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
prefix_sum = [0]

temp = 0
for i in a:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])