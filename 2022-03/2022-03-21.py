# 문제 10026 적록색약

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = []
q = deque()
visit = [[0] * n for _ in range(n)]

for _ in range(n):
    a.append(list(input().strip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solve(x,y):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == a[x][y] and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx,ny])

cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            q.append([i,j])
            solve(i,j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            a[i][j] = 'G'

visit = [[0]*n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            q.append([i,j])
            solve(i,j)
            cnt += 1
print(cnt)