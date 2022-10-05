# 문제 1453 피시방 알바

n = int(input())

a = []
cnt = 0
b = list(map(int, input().split()))

for i in b:
    if i not in a:
        a.append(i)
    else:
        cnt += 1

print(cnt)