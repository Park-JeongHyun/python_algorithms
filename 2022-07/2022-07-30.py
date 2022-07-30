# 문제 2010 플러그

from sys import stdin
input = stdin.readline

n = int(input())
result = 0

for _ in range(n):
    result += int(input())

print(result - n + 1)