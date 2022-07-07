# 문제 1789 수들의 합

s = int(input())
sum = 0
i = 0

while s >= sum:
    i += 1
    sum += i

print(i-1)