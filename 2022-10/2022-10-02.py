# 문제 3047 ABC

a = list(map(int, input().split()))
a.sort()

A = a[0]
B = a[1]
C = a[2]

sequence = input()

for i in sequence:
    if i == "A":
        print(A, end = " ")
    elif i == "B":
        print(B, end = " ")
    else:
        print(C, end = " ")