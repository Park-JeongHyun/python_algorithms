# 문제 10102 개표

n = int(input())

v = input()
cntA = 0
cntB = 0

for i in v:
    if i == "A":
        cntA += 1
    else:
        cntB += 1

if cntA > cntB:
    print("A")
elif cntB > cntA:
    print("B")
else:
    print("Tie")
