# 문제 10984 내 학점을 구해줘

t = int(input())

for _ in range(t):
    n = int(input())
    avg = 0
    c_sum = 0
    total = 0
    for _ in range(n):
        c, g = map(float, input().split())
        c_sum += c
        total += c * g
        avg = total / c_sum
    print(int(c_sum), round(avg, 1))