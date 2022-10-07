# 문제 11943 파일 옮기기

a, b = map(int, input().split())
c, d = map(int, input().split())
cnt = 0

if a + d > b + c:
    cnt = b + c
else:
    cnt = a + d

print(cnt)