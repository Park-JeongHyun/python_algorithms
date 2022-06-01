# 문제 1021 회전하는 큐

from collections import deque

n, m = map(int, input().split())
q = deque([i+1 for i in range(n)])
a = list(map(int, input().split()))

cnt = 0
for i in a:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q)/2:
                while q[0] != i:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)