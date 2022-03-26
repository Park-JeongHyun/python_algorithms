from collections import deque

n = int(input())
k = int(input())
a = [[0] * n for _ in range(n)]

apple = []

for _ in range(k):
    o, p = map(int, input().split())
    a[o-1][p-1] = 1

l = int(input())
info = {}
for _ in range(l):
    x, c = input().split()
    info[int(x)] = c

# input end

def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

# 상,우,하,좌
dy = [-1, 0 ,1, 0]
dx = [0, 1, 0, -1]

def solve():
    direction = 1
    time = 1
    y, x = 0, 0
    visited = deque([[y,x]]) # 꼬리
    a[y][x] = 2

    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < n and 0 <= x < n and a[y][x] != 2:
            if a[y][x] != 1:
                temp_y, temp_x = visited.popleft()
                a[temp_y][temp_x] = 0 # 꼬리 제거
            a[y][x] = 2
            visited.append([y,x])
            if time in info.keys():
                direction = change(direction, info[time])
            time += 1
        else: # 자기 몸이나 벽에 부딪힘
            return time

print(solve())