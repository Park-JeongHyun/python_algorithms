# 문제 15953 상금 헌터

word = input()

for i in word:
    if ord(i) <= 67:
        print(chr(ord(i)+23), end='')
    else:
        print(chr(ord(i)-3), end='')
