# 문제 2875 대회 or 인턴

n, m, k = map(int, input().split())
cnt = 0

while n >= 2 and m >= 1:
    n -= 2
    m -= 1
    cnt += 1

if n + m - k >= 0:
    print(cnt)
else:
    while n + m - k < 0:
        k -= 3
        cnt -= 1
    print(cnt)