# 문제 2864 5와 6의 차이

a, b = map(list, input().split())
tmp_a = a
tmp_b = b

for i in range(len(a)):
    if a[i] == '6':
        tmp_a[i] = '5'

for i in range(len(b)):
    if b[i] == '6':
        tmp_b[i] = '5'

min = int(''.join(tmp_a)) + int(''.join(tmp_b))

for i in range(len(a)):
    if a[i] == '5':
        tmp_a[i] = '6'

for i in range(len(b)):
    if b[i] == '5':
        tmp_b[i] = '6'

max = int(''.join(tmp_a)) + int(''.join(tmp_b))

print(min, max)