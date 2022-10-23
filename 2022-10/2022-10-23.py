# 문제 1264 모음의 개수

arr = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    sen = input()
    cnt = 0
    if sen == "#":
        break
    else:
        for i in sen:
            if i in arr:
                cnt += 1
        print(cnt)