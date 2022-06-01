# 문제 1708 종이의 개수

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

one = 0
zero = 0
minusOne = 0
def solve(x, y, n):
    global one, zero, minusOne

    checkNum = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a[i][j] != checkNum:
                for k in range(3):
                    for l in range(3):
                        solve(x + k * n//3, y + l * n // 3, n // 3)
                return

    if checkNum == -1:
        minusOne += 1
    elif checkNum == 0:
        zero += 1
    else:
        one += 1

solve(0, 0, n)

print(minusOne)
print(zero)
print(one)