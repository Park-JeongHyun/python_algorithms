# 문제 2217 로프

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

def solve():
    a.sort(reverse=True)

    for i in range(n):
        a[i] = a[i] * (i+1)

    return max(a)

print(solve())
