# 문제 2490 윷놀이

for _ in range(3):
    a = list(map(int, input().split()))
    result = sum(a)

    if result  == 0:
        print("D")
    elif result == 1:
        print("C")
    elif result == 2:
        print("B")
    elif result == 3:
        print("A")
    else:
        print("E")
