#문제 2592 대표값

a = []
for _ in range(10):
    a.append(int(input()))

def mode(arr):
    freq = {i:arr.count(i) for i in set(arr)}
    return [i for i in freq.keys() if freq[i] == max(freq.values())]

print(sum(a)//len(a), mode(a)[0])