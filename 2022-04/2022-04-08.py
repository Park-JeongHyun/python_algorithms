# 문제 1934 최소공배수

import sys
input = sys.stdin.readline

# 유클리드 호재법
def gcd(x, y): # 최대공약수
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y): # 최소공배수
    result = (x*y) // gcd(x, y)
    return result

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    print(lcm(x, y))
