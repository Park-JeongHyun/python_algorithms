# 문제 2846 오르막길

n = int(input())

a = list(map(int, input().split()))

max = 0
dp = [a[0]]
# print(dp[-1])
for i in range(1, len(a)):
    if a[i] > dp[-1]:
        dp.append(a[i])
        if dp[-1] - dp[0] > max:
            max = dp[-1] - dp[0]
    else:
        dp = [a[i]]

print(max)