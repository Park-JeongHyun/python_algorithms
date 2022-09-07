# 문제 1297 TV 크기

D, H, W = map(int, input().split())

r = D / ((H**2 + W**2) ** 0.5)

print(int(H*r), int(W*r))