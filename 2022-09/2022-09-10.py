# 문제 1159 농구 경기

n = int(input())
a = []

for _ in range(n):
    word = input()
    a.append(word[0])

b = []
cnt = 0
for i in a:
    if a.count(i) >= 5 and i not in b:
        b.append(i)
        cnt += 1

b.sort()
if cnt == 0:
    print('PREDAJA')
else:
    for i in b:
        print(i, end='')