# 문제 10804 카드 역배치

arr = [j+1 for j in range(20)]

for _ in range(10):
    a, b = map(int, input().split())
    temp = 0
    cnt = b - a
    for i in range(a-1, b-1-(cnt//2)):
        temp = arr[i]
        arr[i] = arr[i + cnt]

        arr[i + cnt] = temp
        cnt -= 2

print(*arr)