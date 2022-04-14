# 문제 1010 다리놓기

t = int(input())

def solve(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for _ in range(t):
    n, m = map(int, input().split())
    print(solve(m) // (solve(n)*solve(m-n)))