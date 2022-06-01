# 문제 2583 영역 구하기

m, n, k = map(int, input().split())

a = [[1] * n for _ in range(m)]
r = []
count = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            a[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(m):
    for j in range(n):
        if a[i][j] == 1:
            cnt = 1
            a[i][j] = 0
            q = [[i, j]]

            while q:
                x, y = q[0][0], q[0][1]
                del q[0]
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < m and 0 <= ny < n and a[nx][ny] == 1:
                        a[nx][ny] = 0
                        cnt += 1
                        q.append([nx,ny])
            count.append(cnt)

print(len(count))
count.sort()
for i in count:
    print(i, end=' ')
