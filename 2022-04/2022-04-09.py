# 문제 2164 카드2

# 시간 248ms
# from collections import deque
#
# n = int(input())
# q = deque([i for i in range(1, n+1)])
#
# while len(q)>1:
#     q.popleft()
#     q.append(q[0])
#     q.popleft()
#
# print(q[0])


# 시간 68ms
n = int(input())
s = 2

while True:
    s *= 2
    if n == 1 or n == 2:
        print(n)
        break
    elif s >= n:
        print((n-(s//2)) * 2)
        break