# 문제 6359 만취한 상범

t = int(input())

for _ in range(t):
    n = int(input())
    a = [1] * n
    for i in range(2, n+1):
        for j in range(n):
            if (j+1) % i == 0 and a[j] == 1:
                a[j] = 0
            elif (j+1) % i == 0 and a[j] == 0:
                a[j] = 1
            else:
                continue

    print(sum(a))