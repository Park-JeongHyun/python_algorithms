# 문제 2501 약수 구하기

n, k = map(int, input().split())

a = []
for i in range(1, n//2 + 1):
    if n % i == 0:
        a.append(i)

a.append(n)
if len(a) >= k:
    print(a[k-1])
else:
    print(0)