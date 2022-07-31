# 문제 2460 지능형 기차 2

maxNum = 0
sumNum = 0

for _ in range(10):
    x, y = map(int, input().split())
    sumNum += y
    sumNum -= x
    if sumNum > maxNum:
        maxNum = sumNum

print(maxNum)