# 문제 11054 가장 긴 바이토닉 부분 수열
n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = dp[i] + dp2[i] - 1

print(max(result))