# 문제 2576 홀수

ans = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        ans.append(num)

if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)

