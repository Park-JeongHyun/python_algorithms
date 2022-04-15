# 문제 2447 별 찍기 -10

n = int(input())

def solve(n):
    if n == 1:
        return ['*']

    s = solve(n//3)
    a = []

    for i in s:
        a.append(i*3)
    for i in s:
        a.append(i + ' '*(n//3) + i)
    for i in s:
        a.append(i*3)

    return a

print('\n'.join(solve(n)))