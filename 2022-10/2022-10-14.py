# 문제 2789 유학 금지

c = "CAMBRIDGE"
word = list(input())

for i in c:
    for j in range(len(word)):
        if i == word[j]:
            word[j] = ''

print(''.join(word))