# 문제 11723 집합

import sys
input = sys.stdin.readline

m = int(input())
s = []

def solve():
    global s

    temp = input().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            s.clear()
            s = [i for i in range(1, 21)]

        elif temp[0] == "empty":
            s.clear()

    else:
        n = int(temp[1])
        if temp[0] == "add" and n not in s:
            s.append(n)
        elif temp[0] == "check":
            if n in s:
                print(1)
            else:
                print(0)
        elif temp[0] == "remove":
            if n in s:
                s.remove(n)
        elif temp[0] == "toggle":
            if n in s:
                s.remove(n)
            else:
                s.append(n)

for _ in range(m):
    solve()
