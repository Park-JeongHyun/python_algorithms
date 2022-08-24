# 문제 3040 백설 공주와 일곱 난쟁이

a = []

for _ in range(9):
    a.append(int(input()))

for i in range(9):
    for j in range(9):
        if i != j:
            temp = sum(a) - a[i] - a[j]
            if temp == 100:
                ans1 = a[i]
                ans2 = a[j]
                break

a.remove(ans1)
a.remove(ans2)

for i in a:
    print(i)