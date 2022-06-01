# 문제 1475 방 번호

n = input()
result = [0]*10

for i in range(len(n)):
    num = int(n[i])

    if num == 6 or num == 9:
        if result[6] >= result[9]:
            result[9] += 1
        else:
            result[6] += 1
    else:
        result[num] += 1

print(max(result))