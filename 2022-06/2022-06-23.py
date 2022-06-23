# 문제 10996 별 찍기 - 21

n = int(input())

a = ["*"]
for _ in range(n):
    if a[-1] == " ":
        a.append("*")
    else:
        a.append(" ")

for i in range(n * 2):
    if i % 2 == 0:
        for j in range(n):
            print(a[j], end="")
        print()
    else:
        for j in range(n):
            print(a[j + 1], end="")
        print()