
from collections import defaultdict
# 約数をリストで返す
def divisor(N):
    i = 1
    l = []
    while i**2 <= N:
        if N % i == 0:
            l.append(i)
            if i**2 != N:
                l.append(N//i)
        i += 1
    return (sorted(l))

N = int(input())
A = list(map(int, input().split()))
B = list(set(A))
B.sort()

d = defaultdict(int)
for i in range(len(B)):
    if i == 2:
        d = dict(d)
    if i <= 1:
        div_list = divisor(B[i])
        for div in div_list:
            d[div] += 1
    else:
        for key in d.keys():
            if B[i] % key == 0:
                d[key] += 1
        k_list = []
        for key, value in d.items():
            if value < i:
                k_list.append(key)
        for key in k_list:
            del d[key]

res_list = []
res = 1
for k, v in d.items():
    if v >= len(B)-1:
        res_list.append(k)
for r in res_list:
    cnt = 0
    for i in range(N):
        if A[i] % r == 0:
            cnt += 1
    if cnt >= N-1:
        res = r
print(res)