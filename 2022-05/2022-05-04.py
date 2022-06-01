# 문제 1992 쿼드트리

n = int(input())
a = [list(map(int, input())) for _ in range(n)]

def solve(x, y, n):
    check = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != a[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        solve(x, y, n)
        solve(x, y+n, n)
        solve(x+n, y, n)
        solve(x+n, y+n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

solve(0, 0, n)