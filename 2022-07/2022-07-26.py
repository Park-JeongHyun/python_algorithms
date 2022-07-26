# 문제 11655 ROT13

s = input()
res = ''

for char in s:
    if 'a' <= char <= 'z':
        res += chr((ord(char)+13) if char <= 'm' else ord(char)-13)
    elif 'A' <= char <= 'Z':
        res += chr((ord(char)+13) if char <= 'M' else ord(char)-13)
    else:
        res += char

print(res)