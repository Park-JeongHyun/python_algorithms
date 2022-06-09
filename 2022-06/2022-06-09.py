# 2003 수들의 합 2

n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while right <= n and left <= right:
    sumNums = a[left:right]
    result = sum(sumNums)

    if result == m:
        cnt += 1
        right += 1

    elif result < m:
        right += 1

    else:
        left += 1

print(cnt)
