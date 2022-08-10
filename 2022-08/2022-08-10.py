# 문제 2587 대표값2

a = []
for _ in range(5):
    a.append(int(input()))

print(sum(a) // 5 )
print(a[2])