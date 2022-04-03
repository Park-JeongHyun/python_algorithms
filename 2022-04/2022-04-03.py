# 문제 1158 요세푸스 문제

n, k = map(int, input().split())
a = []
result = []
cnt = 0

for i in range(1,n+1):
    a.append(i)

for i in range(n):
    cnt += k-1
    if cnt >= len(a):
        cnt %= len(a)
    result.append(a.pop(cnt))

print("<", ', '.join(str(i) for i in result), ">", sep="")