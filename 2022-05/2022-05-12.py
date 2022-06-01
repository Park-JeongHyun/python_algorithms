# 문제 10817 세 수

a, b, c = map(int, input().split())

l = [a, b, c]

l.remove(min(l))
l.remove(max(l))

print(*l)