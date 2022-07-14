# 문제 2953 나는 요리사다

result = 0
cnt = 0
for i in range(5):
    a = list(map(int, input().split()))
    if sum(a) > result:
        cnt = i + 1
        result = sum(a)

print(cnt, result)