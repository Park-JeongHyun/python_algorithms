# 문제 1977 완전제곱수

m = int(input())
n = int(input())

result = []
for i in range(m, n+1):
  if i%(i**(1/2))==0 :
    result.append(i)

if result:
  print(sum(result))
  print(min(result))
else:
  print(-1)