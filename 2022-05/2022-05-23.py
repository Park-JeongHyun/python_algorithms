# 문제 2309 일곱 난쟁이

a = [int(input()) for _ in range(9)]

total = sum(a)

for i in range(9):
    for j in range(i+1, 9):
        if total - (a[i] + a[j]) == 100:
            n1, n2 = a[i], a[j]
            a.remove(n1)
            a.remove(n2)

            a.sort()

            for k in range(len(a)):
                print(a[k])
            break

    if len(a) < 9:
        break