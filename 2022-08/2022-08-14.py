# 문제 2530 인공지능 시계

h, m, s = map(int, input().split())
n = int(input())

if n >= 3600:
    h_temp = n // 3600
    m_temp = n % 3600 // 60
    s_temp = n % 60

    h += h_temp
    m += m_temp
    s += s_temp

elif n >= 60:
    m_temp = n // 60
    s_temp = n % 60

    m += m_temp
    s += s_temp
else:
    s_temp = n
    s += s_temp

if s >= 60:
    s -= 60
    m += 1

if m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h %= 24

print(h, m, s)