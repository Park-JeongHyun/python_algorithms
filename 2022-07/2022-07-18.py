# 문제 10156 과자

k, n, m = map(int, input().split())

if k * n < m:
    print(0)
else:
    print(k * n - m)