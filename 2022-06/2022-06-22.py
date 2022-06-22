# 문제 2455 지능형 기차

sum = 0
max = 0
for _ in range(4):
    minus, plus = map(int, input().split())
    sum += (plus-minus)
    if max < sum:
        max = sum

print(max)
