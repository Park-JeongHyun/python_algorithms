# 문제 1764 듣보잡

n, m = map(int, input().split())
n_list = set()
m_list = set()

for _ in range(n):
    n_list.add(input())

for _ in range(m):
    m_list.add(input())

result = sorted(list(n_list & m_list))

print(len(result))

for i in result:
    print(i)