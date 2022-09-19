# 문제 10448 유레카 이론

t = int(input())
arr = [n*(n+1)//2 for n in range(1, 46)]
result = [0] * 1001

for i in arr:
    for j in arr:
        for k in arr:
            if i + j + k <= 1000:
                result[i + j + k] = 1

for _ in range(t):
    num = int(input())
    print(result[num])