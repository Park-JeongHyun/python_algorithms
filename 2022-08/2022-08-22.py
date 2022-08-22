# 문제 4796 캠핑

cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    if V % P >= L:
        tmp = L
    else:
        tmp = V % P
    print(f"Case {cnt}:", V // P * L + tmp)