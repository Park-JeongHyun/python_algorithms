# 문제 5596 시험 점수

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) > sum(b):
    print(sum(a))
else:
    print(sum(b))