from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())

A, B, C, D = [], [], [], []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

res = 0
pattern = list(combinations_with_replacement(range(1, M+1), N))
for p in pattern:
    tmp = 0
    for i in range(Q):
        if p[B[i]-1] - p[A[i]-1] == C[i]:
            tmp += D[i]
    res = max(res, tmp)
print(res)


