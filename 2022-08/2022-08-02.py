# 문제 10833 사과

a = []
n = int(input())
for _ in range(n):
    school, apple = map(int, input().split())
    a.append([school, apple])

result = 0
for i in range(n):
    result += a[i][1] % a[i][0]

print(result)