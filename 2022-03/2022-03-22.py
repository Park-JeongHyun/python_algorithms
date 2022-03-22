from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = 10000000
house = []
ch = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            house.append((i,j))
        elif a[i][j] == 2:
            ch.append((i,j))

for c in combinations(ch, m):
    temp = 0
    for h in house:
        chi_len = 1000
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += chi_len
    result = min(result, temp)


print(result)