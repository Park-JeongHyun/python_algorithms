import sys
input = sys.stdin.readline
a = []
blank = []


for i in range(9):
    a.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if a[i][j] == 0:
            blank.append((i,j))


def check(x,y):
    key = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if a[x][i] in key:
            key.remove(a[x][i])
        if a[i][y] in key:
            key.remove(a[i][y])

    x1 = x//3
    y1 = y//3

    for i in range(x1 * 3, x1 * 3 + 3):
        for j in range(y1 * 3, y1 * 3 + 3):
            if a[i][j] in key:
                key.remove(a[i][j])

    return key

def solve(n, cnt):

    if n == cnt:
        for i in range(9):
            print(*a[i])
        exit()

    x, y = blank[n]
    for num in check(x, y):
        a[x][y] = num
        solve(n+1, cnt)
        a[x][y] = 0


solve(0, len(blank))