# 문제 2845 파티가 끝나고 난 뒤

l, p = map(int, input().split())
a = []
cnt = list(map(int, input().split()))
for i in cnt:
    a.append(i - (l * p))

print(*a)
