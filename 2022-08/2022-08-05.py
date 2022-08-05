# 문제 7576 그릇

bowl = input()
result = 10

for i in range(len(bowl)-1):
    if bowl[i+1] != bowl[i]:
        result += 10
    else:
        result += 5
print(result)