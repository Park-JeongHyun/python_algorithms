# 문제 4963 섬의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def solve(x, y):
    a[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == 1:
            solve(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    a = []
    cnt = 0
    for _ in range(h):
        a.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                solve(i, j)
                cnt += 1
    print(cnt)