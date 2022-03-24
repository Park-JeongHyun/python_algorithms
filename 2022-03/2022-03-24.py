import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

def solve(x, y, d):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d+3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 청소 해야 하는 곳
        if a[nx][ny] == 0:
            solve(nx, ny, nd)
            return
        # 아니라면 그 방향으로 회전하고, 왼쪽 방향부터 차례대로 인접한 칸을 다시 탐색
        d = nd
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    solve(nx, ny , d)

solve(x, y, d)
print(ans)