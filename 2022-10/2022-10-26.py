# 문제 10768 특별한 날

m = int(input())
d = int(input())

if m < 2 or m == 2 and d < 18:
    print("Before")
elif m > 2 or m == 2 and d > 18:
    print("After")
else:
    print("Special")