# 문제 10953 A+B - 6

t = int(input())

while True:
    try:
        a, b = map(int, input().split(','))
        print(a+b)
    except:
        break