# 문제 11650 좌표 정렬하기

# 시간 4352ms
n = int(input())
a = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append([x,y])

a.sort()

for i in range(n):
    print(*a[i])


# 시간 388ms
import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[0], x[1]))
for i in range(n):
    print(*a[i])