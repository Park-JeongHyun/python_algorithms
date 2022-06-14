# 문제 5585 거스름돈

n = 1000 - int(input())

a = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in a:
    cnt += n//i
    n %= i

print(cnt)