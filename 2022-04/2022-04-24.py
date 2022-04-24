# 문제 4949 균형잡힌 세상

while True:
    s = input()
    st = []
    temp = True

    if s[0] == '.':
        break

    for i in range(len(s)):
        if s[i] == '(':
            st.append(1)
        elif s[i] == '[':
            st.append(2)
        elif s[i] == ')':
            if len(st) > 0 and st[-1] == 1:
                st.pop()
            else:
                temp = False
                break
        elif s[i] == ']':
            if len(st) > 0 and st[-1] == 2:
                st.pop()
            else:
                temp = False
                break

    if temp == True and len(st) == 0:
        print('yes')
    else:
        print('no')
