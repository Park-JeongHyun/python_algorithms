# 문제 2506 점수계산

n = int(input())

a = list(map(int, input().split()))

sum = 0
cnt = 1
for i in range(0, n):
    if i != 0:
        if a[i] == 0:
            cnt = 1
        elif a[i] == 1 and a[i-1] == 0:
            sum += 1
        elif a[i] == 1 and a[i-1] == 1:
            cnt += 1
            sum += cnt
    else:
        if a[i] == 0:
            cnt = 1
        else:
            sum += 1

print(sum)