# 문제 10707 수도요금

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

if P <= C:
    if B > A * P:
        print(A * P)
    else:
        print(B)
else:
    if A * P > (B + (P - C) * D):
        print(B + (P - C) * D)
    else:
        print(A * P)