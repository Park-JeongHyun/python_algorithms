# 문제 2193 이친수

n = int(input())

a = [0, 1, 1]

for i in range(3, 91):
    a.append(a[i-2] + a[i-1])

print(a[n])