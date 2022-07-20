# 문제 5565 영수증

n = int(input())
a = []
for _ in range(9):
    a.append(int(input()))

print(n - sum(a))