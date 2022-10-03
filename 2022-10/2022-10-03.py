# 문제 5355 화성 수학

t = int(input())

for _ in range(t):
    a = list(input().split())
    result = 1
    for i in a:
        if i == " ":
            continue
        elif i == "@":
            result *= 3
        elif i == "%":
            result += 5
        elif i == "#":
            result -= 7
        else:
            result *= float(i)
    print(format(result, ".2f"))