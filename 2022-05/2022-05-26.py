# 문제 11055 가장 큰 증가 부분 수열

n = int(input())

a = list(map(int, input().split()))

dp = [i for i in a]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print((dp))