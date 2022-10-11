# 문제 2720 세탁소 사장 동혁

t = int(input())
q = 25
d = 10
n = 5
p = 1

for _ in range(t):
    c = int(input())

    cnt = 0
    while c >= q:
        c -= q
        cnt += 1
    print(cnt, end=' ')

    cnt = 0
    while c >= d:
        c -= d
        cnt += 1
    print(cnt, end=' ')

    cnt = 0
    while c >= n:
        c -= n
        cnt += 1
    print(cnt, end=' ')

    cnt = 0
    while c >= p:
        c -= p
        cnt += 1
    print(cnt)
