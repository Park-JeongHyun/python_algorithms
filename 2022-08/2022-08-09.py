# 문제 1145 적어도 대부분의 배수

a = list(map(int, input().split()))

n = min(a)
while True:
    cnt = 0
    for i in range(5):
        if n % a[i] == 0:
            cnt += 1
    if cnt > 2:
        print(n)
        break
    n += 1