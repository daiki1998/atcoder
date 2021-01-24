
N, M = map(int, input().split())
S, C = [], []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

res = -1
for i in range(10**N):
    num = str(i)
    if len(num) != N:
        break
