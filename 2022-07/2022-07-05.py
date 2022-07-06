# 문제 10988 팰린드롬인지 확인하기

# p = input()
# a = []
# b = []
#
# for i in range(len(p)):
#     a.append(p[i])
#     b.append(p[-(i+1)])
#
# if a == b:
#     print(1)
# else:
#     print(0)

p = input()

print(1 if p==p[::-1] else 0)