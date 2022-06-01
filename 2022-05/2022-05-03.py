# 문제 2477 참외밭

n = int(input())

x = 0
xi = 0
y = 0
yi = 0

a = []

for i in range(6):
    temp = list(map(int, input().split()))
    a.append(temp)

    if temp[0] == 1 or temp[0] == 2:
        if x < temp[1]:
            x = temp[1]
            xi = i

    else:
        if y < temp[1]:
            y = temp[1]
            yi = i

info = [a[xi-1], a[(xi+1)%6], a[yi-1], a[(yi+1)%6]]

box = 1
for i in a:
    if i not in info:
        box *= i[1]

result = (x*y-box)*n
print(result)