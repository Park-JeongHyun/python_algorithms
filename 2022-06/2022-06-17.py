# 문제 6588 골드바흐의 추측

a = [True for i in range(1000001)]

for i in range(2, 1002):
    if a[i] :
        for k in range(i + i, 1000001, i):
            a[k] = False

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(3, len(a)):
        if a[i] and a[n - i]:
            print(n, "=", i, "+", n - i)
            break