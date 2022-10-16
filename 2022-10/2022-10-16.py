# 문제 2711 오타맨 고창영

t = int(input())

for _ in range(t):
    n, w = input().split()

    a = list(w)
    del a[int(n) - 1]
    print(''.join(a))