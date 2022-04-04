# 문제 1436 영화감독 숌

n = int(input())

x = 666
cnt = 0

while True:
    if '666' in str(x):
        cnt += 1
    if cnt == n:
        print(str(x))
        break
    x += 1
