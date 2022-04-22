# 문제 6603 로또

def solve(depth, idx):
    if depth == 6:
        print(' '.join(map(str, result)))

    for i in range(idx, k):
        result.append(a[i])
        solve(depth+1, i+1)
        result.pop()

while True:
    a = list(map(int, input().split()))
    result = []
    k = a[0]
    if k == 0:
        break
    del a[0]
    solve(0, 0)
    print()