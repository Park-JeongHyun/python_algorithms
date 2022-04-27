# 문제 1182 부분수열의 합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())

a = list(map(int, input().split()))
cnt = 0

def solve(i, result):
    global cnt

    if i >= n:
        return

    result += a[i]

    if result == s:
        cnt += 1

    solve(i+1, result)
    solve(i+1, result - a[i])

solve(0, 0)
print(cnt)