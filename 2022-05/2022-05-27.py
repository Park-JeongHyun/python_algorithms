# 문제 1629 곱셈

a, b, c = map(int, input().split())

def solve(a, n):
    if n == 1:
        return a % c
    else:
        temp = solve(a, n // 2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c

print(solve(a, b))