
N, M = map(int, input().split())
S, C = [], []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)


res = -1
if N == 1:
    l = range(0, 10)
else:
    l = range(10**(N-1), 10**N)
for n in l:
    if all([int(str(n)[S[i]-1]) == C[i] for i in range(M)]):
        res = n
        break
print(res)