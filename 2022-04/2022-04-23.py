# 문제 10799 쇠막대기

a = list(input())
result = 0
st = []

for i in range(len(a)):
    if a[i] == '(':
        st.append(1)
    else:
        if a[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1

print(result)