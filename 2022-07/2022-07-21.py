# 문제 10886 0 = not cute / 1 = cute

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

if sum(a) <= n//2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')