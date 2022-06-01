# 문제 11721 열 개씩 끊어 출력하기

n = input()

for i in range(len(n)):
    print(n[i], end="")
    if (i+1) % 10 == 0:
        print()