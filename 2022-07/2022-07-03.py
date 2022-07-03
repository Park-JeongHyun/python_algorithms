# 문제 1292 쉽게 푸는 문제

a, b = map(int, input().split())

arr = [0]
for i in range(1, b+1):
    for j in range(i):
        arr.append(i)

result = sum(arr[a:b+1])
print(result)