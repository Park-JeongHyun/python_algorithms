# 문제 7562 나이트의 이동

from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, 1, 2, -2, 1, -1]

def solve(n1, n2, j1, j2):
    q = deque()
    q.append((n1, n2))
    a[n1][n2] = 1
    while q:
        x, y = q.popleft()

        if x == j1 and y == j2:
            print(a[j1][j2] - 1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and a[nx][ny] == 0:
                a[nx][ny] = a[x][y] + 1
                q.append((nx,ny))

t = int(input())
for _ in range(t):
    l = int(input())
    a = [[0]*l for _ in range(l)]
    n1, n2 = map(int, input().split())
    j1, j2 = map(int, input().split())
    solve(n1, n2, j1, j2)