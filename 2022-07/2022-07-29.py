# 문제 5554 심부름 가는 길

sum = 0
for i in range(4):
    sum += int(input())

m = sum // 60
s = sum % 60

print(m)
print(s)