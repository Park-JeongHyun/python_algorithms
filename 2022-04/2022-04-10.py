# 문제 10886 덱

import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())

def size():
    return len(q)

def empty():
    if len(q) == 0:
        return 1
    else:
        return 0

for i in range(n):
    cmd = list(input().split())

    if cmd[0] == 'push_front':
        q.appendleft(cmd[1])

    elif cmd[0] == 'push_back':
        q.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            x = q.popleft()
            print(x)

    elif cmd[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            x = q.pop()
            print(x)

    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'empty':
        print(empty())

    elif cmd[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif cmd[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])