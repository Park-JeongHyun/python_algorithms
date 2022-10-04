# 문제 9506 약수들의 합

while True:
    n = int(input())
    a = []
    if n == -1:
        break
    for i in range(1, n//2 + 1):
        if n % i == 0:
            a.append(i)

    if sum(a) == n:
        print(f"{n} = ", end='')
        for j in range(len(a)):
            if j == len(a) - 1:
                print(a[j])
            else:
                print(a[j], "+ ", end='')
    else:
        print(f"{n} is NOT perfect.")