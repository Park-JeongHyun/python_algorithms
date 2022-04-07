# 문제 11729 하노이 탑 이동 순서

n = int(input())

def solve(n, start, end):
    if n == 1:
        print(start, end)
        return
    else:
        solve(n-1, start, 6-start-end)
        print(start, end)
        solve(n-1, 6-start-end, end)

print(2**n-1)
solve(n, 1, 3)
