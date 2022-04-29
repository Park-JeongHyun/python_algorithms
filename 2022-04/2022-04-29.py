# 문제 1476 날짜 계산

e, s, m = map(int, input().split())

e2, s2, m2, cnt = 1,1,1,1

while True:
    if e == e2 and s == s2 and m == m2:
        break
    e2 += 1; s2 += 1; m2 += 1; cnt += 1

    if e2 > 15:
        e2 -= 15
    if s2 > 28:
        s2 -= 28
    if m2 > 19:
        m2 -= 19

print(cnt)