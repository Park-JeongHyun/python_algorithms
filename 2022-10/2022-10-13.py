# 문제 15969 행복

n = int(input())

a = list(map(int, input().split()))

print(max(a) - min(a))